%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Query-Advanced
Summary:	Text::Query::Advanced perl module
Summary(pl):	Modu� perla Text::Query::Advanced
Name:		perl-Text-Query-Advanced
Version:	0.05
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Query::Advanced - matches text against Boolean expression.

%description -l pl
Text::Query::Advanced - wyszukuje tekst stosuj�c operatory logiczne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes readme
%{perl_vendorlib}/Text/Query/Advanced.pm
%{_mandir}/man3/*
