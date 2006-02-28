%define short_name mhchem
%define texhash [ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Eassier writing of chemical formulas and R and S phrases
Summary(pl):	Pakiet u³atwiaj±cy pisanie wzorów chemicznych oraz zwrotów R S
Name:		tetex-latex-%{short_name}
Version:	3.01
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	ftp://ftp.ctan.org//pub/tex/macros/latex/contrib/%{short_name}.zip
# Source0-md5:	41ab7f91f679d0d7a725692093e6e378
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mhchem bundle consists of two packages: mhchem and rsphrase.

The mhchem package provides two commands: one for typesetting chemical
molecular formulae and one for typesetting chemical equations with
these formulae.

The rsphrase package contains the text of all official Risk and Safety
(R and S) Phrases that are used to label chemicals. At the time being,
these phrases are available in English, Danish, French and German
(current spelling).

%description -l pl
Pakiet mhchem sk³ada siê z dwóch pakietów LaTeXowych: mhchem i
rsphrase.

Pakiet mhchem dostarcza dwa polecenia: pierwsze u³atwia pisanie
wzorów chemicznych, drugie umo¿liwia tworzenie równañ chemicznych
przy wykorzystaniu tych wzorów.

Pakiet rsphrase zawiera teksty wszystkich zwrotów R (Risk phrases,
zwroty R, opisuj±ce zagro¿enie) oraz zwrotów S (Safety phrases, zwroty
S, opisuj±ce ¶rodki zapobiegawcze) u¿ywanych do etykietowania zwi±zków
chemicznych. Na chwilê obecn±, zwroty te s± dostêpne w jêzykach:
angielskim, duñskim, francuskim oraz niemieckim (w nowej pisowni).

%prep
%setup -q -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}

install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc whatsnew.txt legal.txt
%doc %{_datadir}/texmf/doc/latex/%{short_name}
%{_datadir}/texmf/tex/latex/%{short_name}
