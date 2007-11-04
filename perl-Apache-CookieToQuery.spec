#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	CookieToQuery
Summary:	Apache::CookieToQuery - rewrite query string by adding cookie information
Summary(pl.UTF-8):	Apache::CookieToQuery - przepisywanie zapytań przez dodawanie informacji o cookie
Name:		perl-Apache-CookieToQuery
Version:	1.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Apache/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec044e95f2de4f1d612a191b640b90e8
URL:		http://search.cpan.org/dist/Apache-CookieToQuery/
BuildRequires:	perl-devel >= 1:5.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-libapreq
BuildRequires:	perl-mod_perl1-devel
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will aid in adding cookie information to your query
strings so that CGI scripts or handlers underneath can have immediate
benefit.

%description -l pl.UTF-8
Ten moduł pomaga w dodawaniu informacji o ciasteczkach do łańcuchów
zapytań, co daje bezpośrednie korzyści skryptom lub procedurom obsługi
CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Apache/*.pm
%{_mandir}/man3/*
