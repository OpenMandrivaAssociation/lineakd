%define name    lineakd
%define version 0.9
%define release %mkrel 4
%define major	0
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:	Control multimedia keys on modern keyboards
License:	GPL
Group:		System/Configuration/Hardware          
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-root
Url:		https://lineak.sourceforge.net/
BuildRequires:	libx11-devel
BuildRequires:	libxtst-devel
Patch0:		lineakd-0.9.0-gcc43.patch
Patch1:		lineakd-0.9.0-link.patch
Requires:	%{libname} = %{version}-%{release}

%description
Daemon to control the multimedia keys on modern keyboards.

Features X11 support, window manager independence, ability to configure
all keys (via a GUI [found in lineakconfig] & .conf file), volume
control, and sound controls.

%package -n %{libname}
Summary:	Libraries needed to run programs linked with %{name}
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Headers for developing programs using %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}lineakd0-devel

%description -n %{develname}
This package contains the headers that programmers will need to develop 
applications which will use %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

rm -fr $RPM_BUILD_ROOT/usr/doc

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc TODO README AUTHORS INSTALL ChangeLog COPYING 
%config(noreplace) %{_sysconfdir}/lineakkb.def
%{_bindir}/%{name}
%{_bindir}/xsendkey*
%{_sbindir}/send_to_keyboard
%{_libdir}/%{name}
%_mandir/*/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/lineak
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
