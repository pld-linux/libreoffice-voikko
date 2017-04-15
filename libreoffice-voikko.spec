Summary:	Multi language spellchecker, grammar checker and hyphenator for LibreOffice
Summary(pl.UTF-8):	Wielojęzyczne narzędzie do sprawdzania pisowni i gramatyki oraz przenoszenia wyrazów dla LibreOffice
Name:		libreoffice-voikko
Version:	5.0
Release:	1
License:	MPL v2.0
Group:		Applications/Text
#Source0Download: https://github.com/voikko/libreoffice-voikko/releases
Source0:	https://github.com/voikko/libreoffice-voikko/archive/rel-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f1f3cbb2fd88a348edee76759bc2533d
URL:		http://voikko.puimula.org/
BuildRequires:	zip
Requires:	libreoffice >= 4.4
Requires:	libreoffice-pyuno >= 4.4
Requires:	libvoikko >= 4.0
Requires:	python3-libvoikko >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libreoffice-voikko is a multi language spellchecker, grammar checker
and hyphenator extension for LibreOffice. It uses libvoikko for all
linguistic operations.

%description -l pl.UTF-8
libreoffice-voikko to obsługujące wiele języków narzędzie do
sprawdzania pisowni i gramatyki oraz przenoszenia wyrazów dla pakietu
biurowego LibreOffice. Do wszystkich operacji językowych wykorzystuje
libvoikko.

%prep
%setup -q -n %{name}-rel-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-unpacked \
	DESTDIR=$RPM_BUILD_ROOT%{_datadir}/libreoffice/share/extensions/voikko

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_datadir}/libreoffice/share/extensions/voikko
%{_datadir}/libreoffice/share/extensions/voikko/META-INF
%{_datadir}/libreoffice/share/extensions/voikko/*.py
%{_datadir}/libreoffice/share/extensions/voikko/*.xcs
%{_datadir}/libreoffice/share/extensions/voikko/*.xcu
%{_datadir}/libreoffice/share/extensions/voikko/*.xdl
%{_datadir}/libreoffice/share/extensions/voikko/*.xml
%{_datadir}/libreoffice/share/extensions/voikko/SettingsDialog_en_US.*
%lang(fi) %{_datadir}/libreoffice/share/extensions/voikko/SettingsDialog_fi_FI.properties
%{_datadir}/libreoffice/share/extensions/voikko/icon.png
%{_datadir}/libreoffice/share/extensions/voikko/voikko.components
