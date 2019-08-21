//MrCZM

var textarea = $('.term');
var speed = 1000; //Writing speed in milliseconds
var text = 'load test && --wish luck';

var i = 0;

runner();

function runner() {
  textarea.append(text.charAt(i));
  i++;
  setTimeout(
    function () {
      if (i < text.length)
        runner();
      else {
        textarea.append("<br>")
        i = 0;
        setTimeout(function () { feedbacker(); }, 1000);
      }
    }, Math.floor(Math.random() * 220) + 50);
}

var count = 0;
var time = 1;
function feedbacker() {
  textarea.append("[    " + count / 1000 + "] " + output[i] + "<br>");
  if (time % 2 == 0) {
    i++;
    textarea.append("[    " + count / 1000 + "] " + output[i] + "<br>");
  }
  if (time == 3) {
    i++;
    textarea.append("[    " + count / 1000 + "] " + output[i] + "<br>");
    i++;
    textarea.append("[    " + count / 1000 + "] " + output[i] + "<br>");
    i++;
    textarea.append("[    " + count / 1000 + "] " + output[i] + "<br>");
  }
  window.scrollTo(0, document.body.scrollHeight);
  i++;
  time = Math.floor(Math.random() * 4) + 1;
  count += time;
  setTimeout(
    function () {
      if (i < output.length - 2)
        feedbacker();
      else {
        textarea.append("<br>Best of Luck...<br>");
        setTimeout(function () { $(".load").fadeOut(1000); }, 500);
      }
    }, time);
}

var output = ["CPU0 microcode updated early to revision 0x1b, date = 2014-05-29",
  "Initializing cgroup subsys cpuset",
  "Initializing cgroup subsys cpu",
  "Initializing cgroup subsys cpuacct",
  "Command line: BOOT_IMAGE=/vmlinuz-3.19.0-21-generic.efi.signed root=UUID=14ac372e-6980-4fe8-b247-fae92d54b0c5 ro quiet splash acpi_enforce_resources=lax intel_pstate=enable rcutree.rcu_idle_gp_delay=1 nouveau.runpm=0 vt.handoff=7",
  "KERNEL supported cpus:",
  "  Intel GenuineIntel",
  "  AMD AuthenticAMD",
  "  Centaur CentaurHauls",
  "e820: BIOS-provided physical RAM map:",
  "BIOS-e820: [mem 0x0000000000000000-0x000000000009dfff] usable",
  "BIOS-e820: [mem 0x000000000009e000-0x000000000009ffff] reserved",
  "BIOS-e820: [mem 0x0000000000100000-0x000000001fffffff] usable",
  "BIOS-e820: [mem 0x0000000020000000-0x00000000201fffff] reserved",
  "BIOS-e820: [mem 0x0000000020200000-0x0000000040003fff] usable",
  "BIOS-e820: [mem 0x0000000040004000-0x0000000040004fff] reserved",
  "BIOS-e820: [mem 0x0000000040005000-0x00000000c9746fff] usable",
  "BIOS-e820: [mem 0x00000000c9747000-0x00000000c9d47fff] ACPI NVS",
  "BIOS-e820: [mem 0x00000000c9d48000-0x00000000c9d4afff] type 20",
  "BIOS-e820: [mem 0x00000000c9d4b000-0x00000000c9d60fff] usable",
  "BIOS-e820: [mem 0x00000000c9d61000-0x00000000c9d66fff] type 20",
  "BIOS-e820: [mem 0x00000000c9d67000-0x00000000c9d68fff] usable",
  "BIOS-e820: [mem 0x00000000c9d69000-0x00000000c9d72fff] type 20",
  "BIOS-e820: [mem 0x00000000c9d73000-0x00000000c9f06fff] usable",
  "BIOS-e820: [mem 0x00000000c9f07000-0x00000000c9f0afff] type 20",
  "BIOS-e820: [mem 0x00000000c9f0b000-0x00000000c9f53fff] usable",
  "BIOS-e820: [mem 0x00000000c9f54000-0x00000000c9f5afff] type 20",
  "BIOS-e820: [mem 0x00000000c9f5b000-0x00000000c9f67fff] reserved",
  "BIOS-e820: [mem 0x00000000c9f68000-0x00000000c9f79fff] type 20",
  "BIOS-e820: [mem 0x00000000c9f7a000-0x00000000c9f7cfff] usable",
  "BIOS-e820: [mem 0x00000000c9f7d000-0x00000000c9f7efff] type 20",
  "BIOS-e820: [mem 0x00000000c9f7f000-0x00000000c9f95fff] usable",
  "BIOS-e820: [mem 0x00000000c9f96000-0x00000000c9f9bfff] type 20",
  "BIOS-e820: [mem 0x00000000c9f9c000-0x00000000c9fa3fff] usable",
  "BIOS-e820: [mem 0x00000000c9fa4000-0x00000000c9fa4fff] type 20",
  "BIOS-e820: [mem 0x00000000c9fa5000-0x00000000c9fb3fff] usable",
  "BIOS-e820: [mem 0x00000000c9fb4000-0x00000000c9fb4fff] type 20",
  "BIOS-e820: [mem 0x00000000c9fb5000-0x00000000c9fbffff] usable",
  "BIOS-e820: [mem 0x00000000c9fc0000-0x00000000c9fc4fff] type 20",
  "BIOS-e820: [mem 0x00000000c9fc5000-0x00000000c9ff0fff] usable",
  "BIOS-e820: [mem 0x00000000c9ff1000-0x00000000c9ff1fff] type 20",
  "BIOS-e820: [mem 0x00000000c9ff2000-0x00000000ca001fff] usable",
  "BIOS-e820: [mem 0x00000000ca002000-0x00000000ca028fff] type 20",
  "BIOS-e820: [mem 0x00000000ca029000-0x00000000ca03cfff] usable",
  "BIOS-e820: [mem 0x00000000ca03d000-0x00000000ca03dfff] type 20",
  "BIOS-e820: [mem 0x00000000ca03e000-0x00000000ca03efff] usable",
  "BIOS-e820: [mem 0x00000000ca03f000-0x00000000ca040fff] type 20",
  "BIOS-e820: [mem 0x00000000ca041000-0x00000000ca041fff] usable",
  "BIOS-e820: [mem 0x00000000ca042000-0x00000000ca046fff] type 20",
  "BIOS-e820: [mem 0x00000000ca047000-0x00000000ca05dfff] usable",
  "BIOS-e820: [mem 0x00000000ca05e000-0x00000000ca0bdfff] reserved",
  "BIOS-e820: [mem 0x00000000ca0be000-0x00000000ca0d7fff] type 20",
  "BIOS-e820: [mem 0x00000000ca0d8000-0x00000000ca601fff] reserved",
  "cfg80211: Calling CRDA to update world regulatory domain",
  "Intel(R) Wireless WiFi driver for Linux, in-tree:",
  "Copyright(c) 2003- 2014 Intel Corporation",
  "iwlwifi 0000:03:00.0: can't disable ASPM; OS doesn't have ASPM control",
  "AVX version of gcm_enc/dec engaged.",
  "AES CTR mode by8 optimization enabled",
  "iwlwifi 0000:03:00.0: loaded firmware version 18.168.6.1 op_mode iwldvm",
  "device-mapper: multipath: version 1.7.0 loaded",
  "[drm] Memory usable by graphics device = 2048M",
  "checking generic (d0000000 7f0000) vs hw (d0000000 10000000)",
  "fb: switching to inteldrmfb from EFI VGA",
  "Console: switching to colour dummy device 80x25",
  "[drm] Replacing VGA console driver",
  "media: Linux media interface: v0.10",
  "Bluetooth: Core ver 2.20",
  "iwlwifi 0000:03:00.0: CONFIG_IWLWIFI_DEBUG disabled",
  "iwlwifi 0000:03:00.0: CONFIG_IWLWIFI_DEBUGFS enabled",
  "iwlwifi 0000:03:00.0: CONFIG_IWLWIFI_DEVICE_TRACING enabled",
  "NET: Registered protocol family 31",
  "Bluetooth: HCI device and connection manager initialized",
  "iwlwifi 0000:03:00.0: Detected Intel(R) Centrino(R) Wireless-N 2230 BGN, REV=0xC8",
  "Bluetooth: HCI socket layer initialized",
  "Bluetooth: L2CAP socket layer initialized",
  "Bluetooth: SCO socket layer initialized",
  "iwlwifi 0000:03:00.0: L1 Enabled - LTR Disabled",
  "Linux video capture interface: v2.00",
  "usbcore: registered new interface driver btusb",
  "intel_rapl: Found RAPL domain package",
  "intel_rapl: Found RAPL domain core",
  "intel_rapl: Found RAPL domain uncore",
  "[drm] Supports vblank timestamp caching Rev 2 (21.10.2013).",
  "[drm] Driver supports precise vblank timestamp query.",
  "vgaarb: device changed decodes: PCI:0000:00:02.0,olddecodes=io+mem,decodes=none:owns=io+mem",
  "gpio_ich: GPIO from 436 to 511 on gpio_ich",
  "cfg80211: World regulatory domain updated:",
  "cfg80211:  DFS Master region: unset",
  "cfg80211:   (start_freq - end_freq @ bandwidth), (max_antenna_gain, max_eirp), (dfs_cac_time)",
  "cfg80211:   (2402000 KHz - 2472000 KHz @ 40000 KHz), (300 mBi, 2000 mBm), (N/A)",
  "cfg80211:   (2457000 KHz - 2482000 KHz @ 40000 KHz), (300 mBi, 2000 mBm), (N/A)",
  "cfg80211:   (2474000 KHz - 2494000 KHz @ 20000 KHz), (300 mBi, 2000 mBm), (N/A)",
  "cfg80211:   (5170000 KHz - 5250000 KHz @ 40000 KHz), (300 mBi, 2000 mBm), (N/A)",
  "cfg80211:   (5735000 KHz - 5835000 KHz @ 40000 KHz), (300 mBi, 2000 mBm), (N/A)",
  "ieee80211 phy0: Selected rate control algorithm 'iwl-agn-rs'",
  "asus_wmi: ASUS WMI generic driver loaded",
  "asus_wmi: Initialization: 0x1",
  "asus_wmi: BIOS WMI version: 7.9",
  "asus_wmi: SFUN value: 0x6a0877",
  "input: Asus WMI hotkeys as /devices/platform/asus-nb-wmi/input/input12",
  "uvcvideo: Found UVC 1.00 device ASUS USB2.0 Webcam (1bcf:2883)",
  "Adding 16760828k swap on /dev/sda5.  Priority:-1 extents:1 across:16760828k SSFS",
  "ACPI: Video Device [PEGP] (multi-head: yes  rom: yes  post: no)",
  "input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/device:02/LNXVIDEO:00/input/input13",
  "ACPI: Video Device [GFX0] (multi-head: yes  rom: no  post: no)",
  "input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:01/input/input14",
  "[drm] Initialized i915 1.6.0 20141121 for 0000:00:02.0 on minor 0",
  "input: ASUS USB2.0 Webcam as /devices/pci0000:00/0000:00:1a.0/usb3/3-1/3-1.3/3-1.3:1.0/input/input15",
  "usbcore: registered new interface driver uvcvideo",
  "USB Video Class driver (1.1.1)",
  "sound hdaudioC0D0: autoconfig: line_outs=2 (0x14/0x16/0x0/0x0/0x0) type:speaker",
  "sound hdaudioC0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)",
  "sound hdaudioC0D0:    hp_outs=1 (0x21/0x0/0x0/0x0/0x0)",
  "sound hdaudioC0D0:    mono: mono_out=0x0",
  "sound hdaudioC0D0:    dig-out=0x1e/0x0",
  "sound hdaudioC0D0:    inputs:",
  "sound hdaudioC0D0:      Internal Mic=0x19",
  "sound hdaudioC0D0:      Mic=0x18",
  "fbcon: inteldrmfb (fb0) is primary device",
  "Console: switching to colour frame buffer device 240x67",
  "i915 0000:00:02.0: fb0: inteldrmfb frame buffer device",
  "i915 0000:00:02.0: registered panic notifier",
  "input: HDA Intel PCH Mic as /devices/pci0000:00/0000:00:1b.0/sound/card0/input16",
  "input: HDA Intel PCH Headphone as /devices/pci0000:00/0000:00:1b.0/sound/card0/input17",
  "asus_wmi: Backlight controlled by ACPI video driver",
  "EXT4-fs (sda4): re-mounted. Opts: errors=remount-ro",
  "systemd-journald[346]: Received request to flush runtime journal from PID 1",
  "EXT4-fs (sda2): mounted filesystem with ordered data mode. Opts: (null)",
  "EXT4-fs (sda7): mounted filesystem with ordered data mode. Opts: (null)",
  "audit: type=1400 audit(1436478108.432:2): apparmor=\"STATUS\" operation=\"profile_load\" profile=\"unconfined\" name=\"/usr/lib/lightdm/lightdm-guest-session\" pid=728 comm=\"apparmor_parser\"",
  "bbswitch: version 0.7",
  "bbswitch: Found integrated VGA device 0000:00:02.0: \_SB_.PCI0.GFX0",
  "bbswitch: Found discrete VGA device 0000:01:00.0: \_SB_.PCI0.PEG0.PEGP",
  "ACPI Warning: \_SB_.PCI0.PEG0.PEGP._DSM: Argument #4 type mismatch - Found [Buffer], ACPI requires [Package] (20141107/nsarguments-95)",
  "bbswitch: detected an Optimus _DSM function",
  "pci 0000:01:00.0: enabling device (0000 -> 0003)",
  "bbswitch: Succesfully loaded. Discrete card 0000:01:00.0 is on",
  "bbswitch: disabling discrete graphics",
  "ACPI Warning: \_SB_.PCI0.PEG0.PEGP._DSM: Argument #4 type mismatch - Found [Buffer], ACPI requires [Package] (20141107/nsarguments-95)",
  "Bluetooth: BNEP (Ethernet Emulation) ver 1.3",
  "Bluetooth: BNEP filters: protocol multicast",
  "Bluetooth: BNEP socket layer initialized",
  "Bluetooth: RFCOMM TTY layer initialized",
  "Bluetooth: RFCOMM socket layer initialized",
  "Bluetooth: RFCOMM ver 1.11",
  "iwlwifi 0000:03:00.0: L1 Enabled - LTR Disabled",
  "iwlwifi 0000:03:00.0: Radio type=0x2-0x0-0x0",
  "iwlwifi 0000:03:00.0: L1 Enabled - LTR Disabled",
  "iwlwifi 0000:03:00.0: Radio type=0x2-0x0-0x0",
  "wlan0: authenticate with 00:90:cc:ea:f4:16",
  "wlan0: send auth to 00:90:cc:ea:f4:16 (try 1/3)",
  "wlan0: authenticated",
  "iwlwifi 0000:03:00.0 wlan0: disabling HT/VHT due to WEP/TKIP use",
  "iwlwifi 0000:03:00.0 wlan0: disabling HT as WMM/QoS is not supported by the AP",
  "iwlwifi 0000:03:00.0 wlan0: disabling VHT as WMM/QoS is not supported by the AP",
  "wlan0: associate with 00:90:cc:ea:f4:16 (try 1/3)",
  "wlan0: RX AssocResp from 00:90:cc:ea:f4:16 (capab=0x431 status=0 aid=3)",
  "wlan0: associated",
  "vboxdrv: Found 8 processor cores.",
  "vboxdrv: fAsync=0 offMin=0x165 offMax=0x24ab",
  "vboxdrv: TSC mode is 'synchronous', kernel timer mode is 'normal'.",
  "vboxdrv: Successfully loaded version 4.3.26_Ubuntu (interface 0x001a000a).",
  "vboxpci: IOMMU not found (not registered)",
  "ip_tables: (C) 2000-2006 Netfilter Core Team",
  "ip6_tables: (C) 2000-2006 Netfilter Core Team",
  "Ebtables v2.0 registered",
  "bridge: automatic filtering via arp/ip/ip6tables has been deprecated. Update your scripts to load br_netfilter if you need this.",
  "device virbr0-nic entered promiscuous mode",
  "nf_conntrack version 0.5.0 (16384 buckets, 65536 max)",
  "virbr0: port 1(virbr0-nic) entered listening state",
  "virbr0: port 1(virbr0-nic) entered listening state",
  "virbr0: port 1(virbr0-nic) entered disabled state",
  "Best of Luck!...", ""];