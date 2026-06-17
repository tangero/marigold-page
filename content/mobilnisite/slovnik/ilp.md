---
slug: "ilp"
url: "/mobilnisite/slovnik/ilp/"
type: "slovnik"
title: "ILP – Inter-Layer Prediction"
date: 2025-01-01
abbr: "ILP"
fullName: "Inter-Layer Prediction"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ilp/"
summary: "Inter-Layer Prediction (ILP) je technika kódování videa používaná v kodeku EVS (Enhanced Voice Services) standardu 3GPP ke zlepšení účinnosti komprese pro škálovatelné datové toky. Predikuje data vyšš"
---

ILP je technika kódování videa v kodeku EVS (Enhanced Voice Services) standardu 3GPP, která predikuje data vyššího rozšiřujícího (enhancement) vrstvy z nižší základní (base) vrstvy za účelem snížení redundance a datového toku pro efektivní přenos v mobilních sítích.

## Popis

Inter-Layer Prediction (ILP) je klíčovou součástí kodeku [EVS](/mobilnisite/slovnik/evs/) (Enhanced Voice Services) standardu 3GPP, konkrétně navrženou pro škálovatelné kódování videa. Funguje v rámci vrstevnaté struktury kódování, kde je video zakódováno do základní vrstvy a jedné či více rozšiřujících vrstev. Základní vrstva poskytuje základní kvalitu při nižším datovém toku, zatímco rozšiřující vrstvy přidávají přírůstková vylepšení kvality. Primární funkcí ILP je využít statistické závislosti mezi těmito vrstvami k dosažení vyšší účinnosti komprese.

Technicky ILP funguje tak, že využívá rekonstruované informace z nižší vrstvy (např. základní vrstvy) k predikci dat pro právě kódovanou rozšiřující vrstvu. Tato predikce může zahrnovat různé typy dat, jako jsou pohybové vektory, transformační koeficienty nebo reziduální signály. Například pohybové vektory ze základní vrstvy mohou být převzorkovány a upřesněny, aby sloužily jako prediktory pro rozšiřující vrstvu, čímž se vyhne nutnosti přenášet zcela nové pohybové informace. Podobně predikce textury využívá jako referenci převzorkovanou rekonstrukci základní vrstvy, takže rozšiřující vrstva potřebuje zakódovat pouze reziduální rozdíl. Tento proces výrazně snižuje datový tok potřebný pro rozšiřující vrstvy ve srovnání s nezávislým kódováním.

Architektura podporující ILP je integrována do nástrojů pro škálovatelné kódování videa kodeku EVS. Mezi klíčové komponenty patří moduly pro predikci vrstev, filtry pro převzorkování pro prostorovou škálovatelnost a mechanismy signalizace predikčních módů. Dekodér provádí odpovídající inverzní predikci s využitím dat základní vrstvy k rekonstrukci rozšiřující vrstvy. ILP je obzvláště účinná ve scénářích vyžadujících adaptivní datový tok, jako je videokonferencing nebo streamovací služby, kde se síťové podmínky mohou měnit. Díky umožnění efektivních vrstevnatých reprezentací umožňuje ILP plynulou adaptaci kvality bez režie více nezávislých kódování, optimalizuje využití přenosové kapacity a zlepšuje uživatelský zážitek v mobilním prostředí.

## K čemu slouží

ILP bylo zavedeno jako odpověď na rostoucí poptávku po kvalitních video službách v mobilních sítích s omezenou a proměnlivou přenosovou kapacitou. Před jeho zavedením škálovatelné kódování videa často trpělo neefektivitou, protože rozšiřující vrstvy byly kódovány nezávisle, což vedlo k významné režii datového toku a sníženým kompresním ziskům. Tato redundance ztěžovala efektivní doručování adaptivních video toků, zejména s rostoucím rozlišením a snímkovou frekvencí videa.

Vytvoření ILP v rámci kodeku [EVS](/mobilnisite/slovnik/evs/) bylo motivováno potřebou efektivnějšího škálovatelného kódovacího rámce, který by mohl podporovat robustní přenos videa v sítích 3GPP. Využitím závislostí mezi vrstvami ILP snižuje datový tok potřebný pro rozšiřující vrstvy, což umožňuje vyšší kvalitu videa při nižších datových tocích nebo plynulejší degradaci kvality při síťovém přetížení. Tato technologie je nezbytná pro aplikace jako videohovory, streamování a vysílací služby, kde je optimalizace přenosové kapacity a adaptace kvality klíčová pro spokojenost uživatelů a správu síťových zdrojů.

## Klíčové vlastnosti

- Umožňuje efektivní predikci dat rozšiřující vrstvy z informací základní vrstvy
- Snižuje režii datového toku ve škálovatelném kódování videa využitím redundance mezi vrstvami
- Podporuje různé typy predikce včetně predikce pohybových vektorů a predikce textury
- Integrováno do kodeku EVS standardu 3GPP pro vylepšenou kompresi videa
- Usnadňuje adaptivní datový tok (streaming) tím, že umožňuje plynulé přepínání vrstev
- Zlepšuje kvalitu videa a využití přenosové kapacity v prostředí mobilních sítí

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [ILP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ilp/)
