Name:    hello
Version: 1.0.0
Release: 1%{?dist}
Summary: Hello world test package
License: MIT
URL:     https://example.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A minimal spec file for testing rpmlint.

%prep

%build

%install

%check

%files
