%define	version   8700b
%define	release   %mkrel 1
%define	dic_date  20070114

# b/c we include the .so for dlopen() in main lib package:
%define _requires_exceptions devel\(.*\) 

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:      anthy
Summary:   A Japanese words input system
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL
URL:       http://www.sourceforge.jp/projects/anthy/
Source0:   http://sourceforge.jp/projects/anthy/files/%{name}-%{version}.tar.gz

# (ut) I modified gcanna.ctd (a dictionary for Anthy).
# http://www.geocities.jp/ep3797/anthy_dict_01.html
Source1:   anthy_gcanna_ut-%{dic_date}.tar.bz2

Patch0:    anthy_name.t.diff

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:        %{libname} = %{version}
BuildRequires:   emacs-bin

%description
Anthy is a free and secure Japanese input system.


%package -n %{libname}
Summary:    Anthy library
Group:      System/Internationalization
Provides:   %{libname_orig} = %{version}-%{release}

%description -n %{libname}
Anthy library.

%package -n %{libname}-devel
Summary:    Headers of %{name} for development
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}
Provides:   %{libname_orig}-devel = %{version}-%{release}

%description -n %{libname}-devel
Anthy development package: static libraries, header files, and the like.


%prep
%setup -q
#%patch0 -p0

# update cannadic
cp %SOURCE1 .
tar -jxf %SOURCE1
cp -f anthy_gcanna_ut-%{dic_date}/gcanna.ctd.%{dic_date} cannadic/gcanna.ctd

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog DIARY NEWS README doc
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/*
%{_datadir}/anthy
#%{_datadir}/emacs/site-lisp/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*
# (tv) fix uim dloading libanthy.so
%{_libdir}/*.so

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*



