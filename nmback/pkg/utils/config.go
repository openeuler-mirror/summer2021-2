package utils

import (
	"github.com/spf13/viper"
	"time"
)

type Config struct {
	CpuThreshold           uint8         `mapstructure:"CPU_ALARM_THRESHOLD"`
	MemThreshold           uint8         `mapstructure:"MEM_ALARM_THRESHOLD"`
	DiskThreshold          uint8         `mapstructure:"DISK_LARM_THRESHOLD"`
	DataCollectionInterval time.Duration `mapstructure:"DATA_COLLECTION_INTERVAL"`
	DelayReminderTime      time.Duration `mapstructure:"DELAY_REMINDER_TIME"`
}

// LoadConfig reads configuration from file or environment variables.
func LoadConfig(path string, configName string, configType string) (config Config, err error) {
	viper.AddConfigPath(path)
	viper.SetConfigName(configName)
	viper.SetConfigType(configType)
	viper.AutomaticEnv()
	viper.WatchConfig()
	err = viper.ReadInConfig()
	if err != nil {
		return
	}
	err = viper.Unmarshal(&config)
	return
}
