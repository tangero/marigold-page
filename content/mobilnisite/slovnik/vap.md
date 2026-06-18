---
slug: "vap"
url: "/mobilnisite/slovnik/vap/"
type: "slovnik"
title: "VAP – Videotex Access Point"
date: 2025-01-01
abbr: "VAP"
fullName: "Videotex Access Point"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vap/"
summary: "Síťová funkční entita definovaná v raných vydáních 3GPP, která poskytuje přístupový bod pro služby Videotexu (známé také jako viewdata). Slouží jako brána mezi mobilními sítěmi a poskytovateli služeb"
---

VAP je síťová funkční entita, která slouží jako brána mezi mobilními sítěmi a poskytovateli služeb Videotexu a umožňuje přístup k informačním a transakčním službám.

## Popis

Videotex Access Point (VAP) je zastaralá komponenta servisní architektury definovaná v éře okruhově přepínaných datových služeb. Funguje jako specializovaná brána nebo přístupový uzel v rámci Core Network určený výhradně pro aplikaci Videotex. Videotex je interaktivní systém pro vyhledávání informací, který umožňuje uživatelům přistupovat ke stránkám textu a jednoduché grafiky z vzdálených databází prostřednictvím terminálu. V mobilním kontextu VAP poskytuje potřebné rozhraní a adaptaci protokolů, aby umožnil mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) připojit se k hostitelskému počítači poskytovatele služeb Videotexu.

Architektonicky se VAP nachází v rámci síťové domény, na jedné straně komunikuje s jádrem mobilní sítě (typicky přes [MSC](/mobilnisite/slovnik/msc/) nebo přímo s datovou sítí) a na druhé straně s externími poskytovateli služeb Videotexu. Mezi jeho klíčové komponenty patří protokolové zásobníky pro zpracování připojení na straně mobilní sítě (např. využívající okruhově přepínané datové přenosy) a připojení na straně Videotexu, které historicky používalo protokoly jako Videotex Access Protocol (VAP) samotný nebo jiné standardizované viewdata protokoly. Spravuje navázání relace, autentizaci uživatele, výběr služby a konverzi formátování dat mezi možnostmi mobilního terminálu a požadavky hostitelského systému Videotexu.

Jak funguje: mobilní uživatel zahájí datové volání. Namísto připojení ke standardní modémové sadě nebo poskytovateli internetových služeb ([ISP](/mobilnisite/slovnik/isp/)) je volání směrováno na VAP na základě volaného čísla nebo servisního kódu. VAP přijme volání, provede případnou nezbytnou autentizaci a vyjednávání služby s mobilním uživatelem a poté naváže spojení s vybraným poskytovatelem služeb Videotexu. Slouží jako přenosný prvek, který překládá mezi datovými formáty a řídicími signály používanými v mobilním spojení a těmi používanými ve fixní síti Videotexu. Jeho úlohou bylo odstínit složitost mobilní sítě od poskytovatele služeb Videotexu a poskytnout standardizovaný, řízený přístupový bod pro mobilní účastníky využívající tyto předwebové informační služby.

## K čemu slouží

VAP byl vytvořen za účelem umožnění nabídky služeb Videotexu přes rané digitální mobilní sítě, jako je GSM. V pozdních 80. a 90. letech 20. století byl Videotex (např. Prestel, Minitel) oblíbenou metodou přístupu k online informacím, bankovnictví a nakupování z pevných terminálů. S růstem mobilní telefonie existoval komerční motiv rozšířit tyto přidané služby na mobilní účastníky. VAP poskytl potřebné standardizované rozhraní pro integraci těchto existujících, rozsáhlých ekosystémů služeb Videotexu s novou infrastrukturou mobilních sítí.

Řešil problém interoperability. Bez standardizovaného přístupového bodu by každý mobilní operátor musel vyvíjet vlastní brány pro každého poskytovatele Videotexu a každý poskytovatel Videotexu by musel rozumět složitost signalizace mobilní sítě. Specifikace VAP vytvořila jasný demarkační bod a definovanou sadu procedur. Řešila omezení pouhého využití modémové sady, protože služby Videotexu často vyžadovaly specifickou správu relací, rozhraní pro účtování a zpracování protokolů, které obecná datová připojení neposkytovala. VAP umožnil vytvoření životaschopného obchodního modelu pro mobilní Videotex definováním způsobu, jak lze využití sledovat a účtovat odděleně od standardních hlasových hovorů.

## Klíčové vlastnosti

- Funkce brány mezi mobilní sítí a poskytovateli služeb Videotexu
- Spravuje řízení relace pro interaktivní aplikace Videotexu
- Zpracovává autentizaci uživatele a autorizaci služby
- Poskytuje adaptaci protokolů mezi mobilními a Videotex protokoly
- Podporuje účtování specifické pro službu a generování účetních dat
- Definován jako standardizovaná síťová funkční entita pro interoperabilitu

## Související pojmy

- [USAT – Universal Subscriber Identity Module Application Toolkit](/mobilnisite/slovnik/usat/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.043** (Rel-4) — GSM Videotex Service Support

---

📖 **Anglický originál a plná specifikace:** [VAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/vap/)
