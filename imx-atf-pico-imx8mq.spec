Name: imx-atf-imx8mq
Version: 5.4.70
Release: alt1

Summary: ARM Trusted Firmware for TechNexion IMX8MQ platform
License: BSD
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

%description
ARM Trusted Firmware provides a reference implementation of secure world
software for ARMv8-A, including a Secure Monitor executing at
Exception Level 3 (EL3). It implements various ARM interface standards, such as:

-  The Power State Coordination Interface (PSCI)
-  Trusted Board Boot Requirements (TBBR, ARM DEN0006C-1)
-  SMC Calling Convention
-  System Control and Management Interface

As far as possible the code is designed for reuse or porting to other ARMv8-A
model and hardware platforms.

ARM will continue development in collaboration with interested parties to
provide a full reference implementation of Secure Monitor code and ARM standards
to the benefit of all developers working with ARMv8-A TrustZone technology.

%prep
%setup

%build
%make_build PLAT=imx8mq bl31

%install
install -pm0644 -D build/imx8mq/release/bl31.bin %buildroot%_datadir/atf/imx8mq/bl31.bin

%files
%_datadir/atf

%changelog
* Mon May 24 2021 Pavel Nakonechnyi <zorg@altlinux.org> 5.4.70-alt1
- switched to imx_5.4.70_2.3.0 branch

* Tue Oct 27 2020 Pavel Nakonechnyi <zorg@altlinux.org> 4.14.98-alt2
- updated to 413e93e1 commit of the upstream

* Sun Jul 07 2019 Pavel Nakonechnyi <zorg@altlinux.org> 4.14.98-alt1
- initial build of ARM Trusted Firmware backed for TechNexion IMX8MQ platform
