//
package main

import (
	"flag"
	"log"
	"strings"
	"time"

	S "monitor-notify/pkg/utils"
)

var configPath, configName string

func init() {
	log.Println("Begin to parase command flag")
	flag.StringVar(&configPath, "configpath", "/home/openeuler/Desktop/nm/nmback/configs/", "config file dir")
	flag.StringVar(&configName, "configfile", "nmconfig.yaml", "config file name")
}

func main() {
	flag.Parse()
	log.Println("Parse configname")
	configFile := strings.Split(configName, ".")
	log.Println("Config name os ",configFile)
	var config S.Config
	log.Println("Load config from ",configPath)
	config, _ = S.LoadConfig(configPath, configFile[0], configFile[1])
	log.Println("Begin to create ticker")
	ticker := time.NewTicker(config.DataCollectionInterval)
	count := 1
	for range ticker.C {
		log.Println("Get system info")
		if S.GetMemPercent() >= int((config.MemThreshold)) || S.GetCpuPercent() >= int(config.CpuThreshold) || S.GetDiskPercent() >= int(config.DiskThreshold) {
			if count == 1 {
				log.Println("reminder")
				S.DeepinNotify()
				log.Println("Reset conter")
				count = int(config.DelayReminderTime.Seconds() / config.DataCollectionInterval.Seconds())
			} else {
				count--
				log.Println("Delayed reminder")
			}
		}else {
			log.Println("Sufficient system resources")
		}
	}
}
