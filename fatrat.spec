%define name fatrat
%define version 1.1.2
%define release %mkrel 2

Summary: Wownload manager for Linux with the help of the Trolltech Qt 4 library.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPLv2
Group: Networking/File transfer
Url:   http://fatrat.dolezel.info/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libqt4-devel 
BuildRequires: libssh2-devel 
BuildRequires: libtorrent-rasterbar-devel
BuildRequires: cmake 
BuildRequires: libgloox-devel
BuildRequires: libqtscript4
BuildRequires: libboost-devel

Requires: libtorrent-rasterbar5
Requires: qt4-common
Requires: libssh2_1

Suggests: fatrat-czshare
Suggests: fatrat-opensubtitles
Suggests: fatrat-unpack

%description
FatRat is an open source download manager for Linux/Unix systems written in C++ with the help of the Trolltech Qt 4 library. It is rich in features and is continuously developed.

%package devel
Summary:        C development headers for enet
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains header files required for development.


%prep
%setup -q

%build
cmake . -DWITH_BITTORRENT=ON -DWITH_SFTP=ON -DWITH_CURL=ON -DWITH_ZIP=ON -DWITH_JABBER=ON -DWITH_NLS=ON  -DWITH_WEBINTERFACE=ON -DCMAKE_INSTALL_PREFIX=%{_prefix}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_datadir}/%{name}/AUTHORS
%{_datadir}/%{name}/INSTALL
%{_datadir}/%{name}/LICENSE
%{_datadir}/%{name}/README
%{_datadir}/%{name}/TRANSLATIONS
%{_bindir}/fatrat
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/lang/*.qm
%{_datadir}/%{name}/data/css/*
%{_datadir}/%{name}/data/btlinks.txt
%{_datadir}/%{name}/data/btsearch.xml
%{_datadir}/%{name}/data/defaults.conf
%{_mandir}/man1/%{name}*
%{_datadir}/%{name}/data/remote/*


%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}/*

%changelog
