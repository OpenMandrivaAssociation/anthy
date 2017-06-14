%define dic_date  20110409
%define major	0
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:		anthy
Summary:	A Japanese words input system
Version:	9100h
Release:	25.%{dic_date}.5
Group:		System/Internationalization
License:	GPLv2+
Url:		http://www.geocities.jp/ep3797/anthy_dict_01.html
Source0:	http://sourceforge.net/projects/mdk-ut/files/30-source/source/%{name}-%{version}-%{dic_date}ut.tar.bz2

BuildRequires:	emacs-bin

%description
Anthy is a free and secure Japanese input system.

%package -n %{libname}
Summary:	Anthy library
Group:		System/Libraries

%description -n %{libname}
Anthy library.

%package -n %{devname}
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Anthy development libraries, header files, and the like.

%prep
%setup -qn %{name}-%{version}-%{dic_date}ut

%build
export CC=gcc
export CXX=g++

%configure --disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS DIARY NEWS README doc
%config %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/anthy
%{_datadir}/emacs/site-lisp/anthy/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc COPYING
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
