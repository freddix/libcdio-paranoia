Summary:	CD paranoia CD-DA libraries from libcdio
Name:		libcdio-paranoia
Version:	0.90
Release:	2
License:	LGPL v2.1 (library), GPL v2 (utility)
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/libcdio/%{name}-10.2+%{version}.tar.gz
# Source0-md5:	7175764764c7fa22e1b802b9526c9411
Patch0:		%{name}-headers.patch
URL:		http://www.gnu.org/software/libcdio/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	help2man
BuildRequires:	libcdio-devel >= 0.90
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This CDDA reader distribution ('libcdio-cdparanoia') reads audio from
the CDROM directly as data, with no analog step between, and writes
the data to a file or pipe as .wav, .aifc or as raw 16 bit linear PCM.

%package devel
Summary:	Header files for libcdio-paranoia libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcdio-devel >= 0.90

%description devel
Header files for libcdio-paranoia libraries.

%package utils
Summary:	libcdio-paranoia utility: cd-paranoia
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description utils
libcdio-paranoia utility: cd-paranoia.

%prep
%setup -qn  %{name}-10.2+%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-maintainer-mode \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS doc/FAQ.txt
%attr(755,root,root) %ghost %{_libdir}/libcdio_cdda.so.1
%attr(755,root,root) %ghost %{_libdir}/libcdio_paranoia.so.1
%attr(755,root,root) %{_libdir}/libcdio_cdda.so.*.*.*
%attr(755,root,root) %{_libdir}/libcdio_paranoia.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdio_cdda.so
%attr(755,root,root) %{_libdir}/libcdio_paranoia.so
%{_includedir}/cdio/paranoia
%{_pkgconfigdir}/libcdio_cdda.pc
%{_pkgconfigdir}/libcdio_paranoia.pc

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cd-paranoia
%{_mandir}/man1/cd-paranoia.1*

