class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __del__(self):
        print(f"Об'єкт TimeConverter для {self.hours}:{self.minutes}:{self.seconds} видалено.")
    
    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def get_time(self):
        return (self.hours, self.minutes, self.seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def from_seconds(self, total_seconds):
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60
    
    def output_converted_time(self, time_format="seconds"):
        if time_format == "seconds":
            print(f"Час у секундах: {self.to_seconds()}")
        elif time_format == "hh:mm:ss":
            print(f"Час у форматі hh:mm:ss: {self.hours:02}:{self.minutes:02}:{self.seconds:02}")
        else:
            print("Невірний формат виведення.")

def main():
    time_converter = TimeConverter(1, 30, 45)
    
    time_converter.output_converted_time("hh:mm:ss")
    
    time_converter.output_converted_time("seconds")
    
    time_converter.output_converted_time("seconds")
    
    time_converter.set_time(2, 15, 30)

    time_converter.output_converted_time("hh:mm:ss")
    
    time_converter.output_converted_time("seconds")

if __name__ == "__main__":
    main()
### yarema loh i vanychka :)
