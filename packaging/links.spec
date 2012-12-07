Name:           links
BuildRequires:  automake
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
Url:            http://artax.karlin.mff.cuni.cz/~mikulas/links/
Provides:       web_browser
Version:        2.6
Release:        0
Summary:        Text-Based WWW Browser
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Browsers
Source:         links-%{version}.tar.bz2

%description
Links is like Lynx--an easy-to-use browser for HTML documents and other
Internet services, like FTP, telnet, and news. Links provides a
graphical interface besides the text interface. It has good support for
frames, supports ssl, and has a little bit of JavaScript support.


%prep
%setup -q -n links-%{version}
%patch2

%build
autoreconf -ifv
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -pipe"
%configure  --with-ssl  --with-pic
make

%install
mkdir -p $RPM_BUILD_ROOT/{%{_mandir}/man1,usr/bin,%{_infodir}} 
cp links.1 $RPM_BUILD_ROOT/%{_mandir}/man1
make install DESTDIR=$RPM_BUILD_ROOT
make clean
make EXTRAA="-DSHOW_COLOR=TRUE"
install links $RPM_BUILD_ROOT/usr/bin/links

%files
%defattr(-,root,root)
/usr/bin/links
%doc %{_mandir}/man1/links.1.gz

%changelog
