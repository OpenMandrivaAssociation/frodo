%define name    frodo
%define version 4.2
%define cvsdate 20030707
%define rel %mkrel 4
%define release 0.%{cvsdate}.%{rel}

Summary:       Free portable C64 emulator
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       Frodo4-%{cvsdate}.tar.bz2
Source10:      Frodo.16.png
Source11:      Frodo.32.png
Source12:      Frodo.48.png
License:       GPLv2
Group:         Emulators
Url:           http://frodo.cebix.net/
BuildRoot:     %{_tmppath}/%{name}-buildroot
BuildRequires: SDL-devel >= 1.2.0

%description
Frodo is a free, portable Commodore 64 emulator that runs on a variety
of platforms, with a focus on the exact reproduction of special graphical
effects possible on the C64.

Frodo comes in three flavours: The "normal" Frodo with a line-based
emulation, the improved line-based emulation "Frodo PC", and the
single-cycle emulation "Frodo SC" that is slower but far more compatible.

%prep
%setup -q -n Frodo4

%build
cd Src
%configure2_5x
%make

%install
rm -rf %{buildroot}
cd Src
%makeinstall_std

cd ..
mkdir -p %{buildroot}%{_datadir}/frodo/64prgs
rm -rf 64prgs/CVS
install -m644 64prgs/* %{buildroot}%{_datadir}/frodo/64prgs/

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Frodo
Comment=C64 Emulator, Classic Line Mode
Exec=Frodo
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Emulators;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}-pc.desktop << EOF
[Desktop Entry]
Name=FrodoPC
Comment=C64 Emulator, Improved Line Mode
Exec=Frodo
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Emulators;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}-sc.desktop << EOF
[Desktop Entry]
Name=FrodoSC
Comment=C64 Emulator, Single-Cycle Mode
Exec=Frodo
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Emulators;
EOF

install -m644 %{SOURCE10} %{buildroot}%{_miconsdir}/frodo.png
install -m644 %{SOURCE11} %{buildroot}%{_iconsdir}/frodo.png
install -m644 %{SOURCE12} %{buildroot}%{_liconsdir}/frodo.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}

%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc COPYING CHANGES 
%doc Docs/*.html
%{_bindir}/Frodo
%{_bindir}/FrodoPC
%{_bindir}/FrodoSC
%{_bindir}/Frodo_GUI.tcl
"%{_datadir}/frodo/1541 ROM"
"%{_datadir}/frodo/Basic ROM"
"%{_datadir}/frodo/Char ROM"
"%{_datadir}/frodo/Kernal ROM"
%{_datadir}/frodo/64prgs
%{_miconsdir}/frodo.png
%{_iconsdir}/frodo.png
%{_liconsdir}/frodo.png
%{_datadir}/applications/mandriva-%{name}*.desktop



%changelog
* Sun Jul 31 2011 Andrey Bondrov <abondrov@mandriva.org> 4.2-0.20030707.4mdv2012.0
+ Revision: 692544
- imported package frodo


* Sun Jul 24 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 4.2-0.20030707.4mdv2011.0
- Import from PLF
- Remove PLF reference

* Sun Aug 20 2006 Olivier Thauvin <nanardon@zarb.org> 4.2-0.20030707.3plf
- xdg menu

* Sun Apr 10 2005 Sylvie Terjan <erinmargault@zarb.org> 4.2-0.20030707.2plf
- rebuild for SDL-devel
- add plf reason
- remove redundant prefix tag

* Mon Dec 22 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.2-0.20030707.1plf
- plf introduction

* Sat Jul 05 2003 andi payn <payn@myrealbox.com> 4.2-0.20030707.1mdk
- CVS version (now GPL'd), essentially a 4.2rc except for docs
- borrowed heavily from new specfile in package

* Sat Jul 05 2003 andi payn <payn@myrealbox.com> 4.1b-1mdk
- Initial package

# end of file
