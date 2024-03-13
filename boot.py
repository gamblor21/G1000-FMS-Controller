# boot.py
import usb_hid

SIM_JOYSTICK_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,    # UsagePage(Generic Desktop[0x0001])
    0x09, 0x04,    # UsageId(Joystick[0x0004])
    0xA1, 0x01,    # Collection(Application)
    0x85, 0x01,    #     ReportId(1)
    0x05, 0x09,    #     UsagePage(Button[0x0009])
    0x19, 0x01,    #     UsageIdMin(Button 1[0x0001])
    0x29, 0x05,    #//     UsageIdMax(Button 5[0x0005])
    0x15, 0x00,    #//     LogicalMinimum(0)
    0x25, 0x01,    #//     LogicalMaximum(1)
    0x95, 0x05,    #//     ReportCount(5)
    0x75, 0x01,    #//     ReportSize(1)
    0x81, 0x02,    #//     Input(Data, Variable, Absolute, NoWrap, Linear, PreferredState, NoNullPosition, BitField)
    0x95, 0x01,    #//     ReportCount(1)
    0x75, 0x03,    #//     ReportSize(3)
    0x81, 0x03,    #//     Input(Constant, Variable, Absolute, NoWrap, Linear, PreferredState, NoNullPosition, BitField)
    0x19, 0x06,    #//     UsageIdMin(Button 6[0x0006])
    0x29, 0x0B,    #//     UsageIdMax(Button 11[0x000B])
    0x95, 0x06,    #//     ReportCount(6)
    0x75, 0x01,    #//     ReportSize(1)
    0x81, 0x02,    #//     Input(Data, Variable, Absolute, NoWrap, Linear, PreferredState, NoNullPosition, BitField)
    0x95, 0x01,    #//     ReportCount(1)
    0x75, 0x02,    #//     ReportSize(2)
    0x81, 0x03,    #//     Input(Constant, Variable, Absolute, NoWrap, Linear, PreferredState, NoNullPosition, BitField)
    0xC0,          #// EndCollection()
))

sim_joystick = usb_hid.Device(
    report_descriptor=SIM_JOYSTICK_REPORT_DESCRIPTOR,
    usage_page=0x01,           # Generic Desktop Control
    usage=0x04,                # Joystick
    report_ids=(1,),           # Descriptor uses report ID 1.
    in_report_lengths=(2,),    # This controller sends 2 bytes in its report.
    out_report_lengths=(0,),   # It does not receive any reports.
)

usb_hid.enable(
    (sim_joystick,
    )
)
