package utils

import (
	"log"
	"time"

	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/disk"
	"github.com/shirou/gopsutil/mem"
)

func GetMemPercent() int {
	vm, _ := mem.VirtualMemory()
	log.Println("mem percent is ",vm.UsedPercent)
	return int(vm.UsedPercent)
}

func GetDiskPercent() int {
	diskInfo, _ := disk.Usage("/")
	log.Println("disk percent is ",diskInfo.UsedPercent)
	return int(diskInfo.UsedPercent)
}

func GetCpuPercent() int {
	cpuInfo, _ := cpu.Percent(time.Second, false)
	log.Println("cpu percent is ",cpuInfo[0])
	return int(cpuInfo[0])
}
