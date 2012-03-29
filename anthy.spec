%define	version   9100h
%define	dic_date  20110409

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %name

Name:      anthy
Summary:   A Japanese words input system
Version:   %{version}
Release:   25.%{dic_date}.1
Group:     System/Internationalization
License:   GPLv2+
URL:	http://www.geocities.jp/ep3797/index.html
# http://www.geocities.jp/ep3797/anthy_dict_01.html
Source0:   http://ovh.dl.sourceforge.net/sourceforge/mdk-ut/anthy/anthy-%{version}-%{dic_date}ut.tar.bz2

Requires:        %{libname} = %{version}
BuildRequires:   emacs-bin automake

%description
Anthy is a free and secure Japanese input system.


%package -n %{libname}
Summary:    Anthy library
Group:      System/Internationalization

%description -n %{libname}
Anthy library.

%package -n %{develname}
Summary:    Headers of %{name} for development
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}
Obsoletes:  %mklibname -d anthy 0
Conflicts:  %{mklibname anthy 0} < 9100e-10

%description -n %{develname}
Anthy development package: static libraries, header files, and the like.


%prep
%setup -q -n %{name}-%{version}-%{dic_date}ut

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog DIARY NEWS README doc
%{_bindir}/*
%config %{_sysconfdir}/*
%{_datadir}/anthy
%{_datadir}/emacs/site-lisp/anthy/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
