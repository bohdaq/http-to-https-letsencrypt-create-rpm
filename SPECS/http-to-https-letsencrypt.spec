%define _topdir    /Users/bogdantsap/git/http-to-https-letsencrypt-create-rpm
%define name       http-to-https-letsencrypt
%define release    0
%define version    8.0.0
%define buildroot  %{_topdir}/%{name}-%{version}-root

BuildRoot:         %{buildroot}
Summary:           http-to-https-letsencrypt
License:           MIT
Name:              %{name}
Version:           %{version}
Release:           %{release}
Source:            %{name}-%{version}.tar.gz
Prefix:            /usr
Group:             Development/Tools

%description
http-to-https-letsencrypt is an application web-server for making permanent redirects from http to https.

%prep
%setup -q

%build
cargo test

%install
rustup override set nightly
cargo build -Zunstable-options --release  --out-dir $RPM_BUILD_ROOT/usr/local/bin

%files
%defattr(-, root, root)
/usr/local/bin/http-to-https-letsencrypt

