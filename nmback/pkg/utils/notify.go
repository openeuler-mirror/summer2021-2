package utils

import (
	"log"
	"os"
	"os/exec"
	"sync"

	"github.com/esiqveland/notify"
	"github.com/godbus/dbus/v5"
)

func DeepinNotify() {
	wg := &sync.WaitGroup{}

	conn, err := dbus.SessionBusPrivate()
	if err != nil {
		panic(err)
	}
	defer conn.Close()

	if err = conn.Auth(nil); err != nil {
		panic(err)
	}

	if err = conn.Hello(); err != nil {
		panic(err)
	}
	// Basic usage
	// Create a Notification to send
	iconName := "notifymonitor"
	n := notify.Notification{
		AppName:       "System notify",
		ReplacesID:    uint32(0),
		AppIcon:       iconName,
		Summary:       "Warning",
		Body:          "System resources usage has reached the threshold.",
		Actions:       []string{"cancel", "Remind later", "detail", "Details"},
		Hints:         map[string]dbus.Variant{},
		ExpireTimeout: int32(5000000),
	}

	// Ship it!
	createdID, err := notify.SendNotification(conn, n)
	if err != nil {
		log.Printf("error sending notification: %v", err.Error())
	}
	log.Printf("created notification with id: %v", createdID)
	onAction := func(action *notify.ActionInvokedSignal) {
		if action.ActionKey == "detail" {
			sendCmd := "deepin-system-monitor"
			sendCmdLong := exec.Command(sendCmd)
			sendCmdLong.Start()
		}
		log.Printf("ActionInvoked: %v Key: %v", action.ID, action.ActionKey)
		wg.Done()
	}

	onClosed := func(closer *notify.NotificationClosedSignal) {
		log.Printf("NotificationClosed: %v Reason: %v", closer.ID, closer.Reason)
	}

	// Notifier interface with event delivery
	notifier, err := notify.New(
		conn,
		// action event handler
		notify.WithOnAction(onAction),
		// closed event handler
		notify.WithOnClosed(onClosed),
		// override with custom logger
		notify.WithLogger(log.New(os.Stdout, "notify: ", log.Flags())),
	)
	if err != nil {
		log.Fatalln(err.Error())
	}
	defer notifier.Close()
	wg.Add(1)
	wg.Wait()
}
