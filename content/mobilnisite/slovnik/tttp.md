---
slug: "tttp"
url: "/mobilnisite/slovnik/tttp/"
type: "slovnik"
title: "TTTP – Transfer To Third Party"
date: 2025-01-01
abbr: "TTTP"
fullName: "Transfer To Third Party"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tttp/"
summary: "Doplňková služba umožňující uživateli převést probíhající hovor na třetí stranu. Jde o síťovou funkci usnadňující správu a přesměrování hovorů, která zvyšuje kontrolu uživatele nad komunikačními relac"
---

TTTP je doplňková služba, která umožňuje uživateli převést probíhající hovor na třetí stranu v rámci okruhově přepínané domény.

## Popis

Transfer To Third Party (TTTP, přenos na třetí stranu) je doplňková služba okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) domény standardizovaná organizací 3GPP. Umožňuje obsluhovanému uživateli (Uživatel A), který vede aktivní hovor s jinou stranou (Uživatel B), převést tento hovor na třetí stranu (Uživatel C). Službu vyvolá Uživatel A, obvykle prostřednictvím specifického postupu, jako je např. přidržení Uživatele B, navázání nového hovoru s Uživatelem C a následné zahájení přenosu. Síť poté spojí Uživatele B a Uživatele C přímo a uvolní Uživatele A z připojení. Tato služba se liší od přesměrování hovoru (call forwarding), které funguje u příchozích hovorů před jejich přijetím; TTTP pracuje s již navázaným, aktivním hovorem.

Architektura služby je založena na schopnostech ústředny mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)) a registru domovské lokace ([HLR](/mobilnisite/slovnik/hlr/)) v CS jádru sítě. HLR uchovává profil služeb účastníka, který udává, zda je TTTP zřízeno. Když uživatel přenos zahájí, obsluhující MSC provede servisní logiku. Ta zahrnuje správu více větví hovoru: původní větve (A-B), konzultační větve (A-C) a nakonec navázání nové větve (B-C) při současném uvolnění větví zahrnujících Uživatele A. Služba používá standardní signalizaci [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo protokoly Bearer Independent Call Control (BICC) pro správu těchto spojení mezi síťovými uzly.

Z pohledu signalizace proces zahrnuje specifické zprávy a postupy definované ve specifikacích jádra sítě. Uživatel obvykle zadá číslo třetí strany pomocí [DTMF](/mobilnisite/slovnik/dtmf/) tónů nebo událostí flash-hook. MSC to interpretuje jako žádost o službu, pozastaví původní hovor a zahájí nové sestavení hovoru. Po úspěšném připojení k třetí straně MSC provede operaci spojení (connect), aby propojila dvě vzdálené strany. Klíčovým aspektem je zajištění správného účtování; servisní logika musí správně přiřadit segmenty hovoru příslušným stranám, což často zahrnuje specifické účtovací triggery a záznamy.

Úlohou TTTP je poskytovat pokročilé řízení hovoru, což je funkce převzatá z pevných ISDN služeb do mobilních sítí. Je součástí souboru doplňkových služeb obohacujících základní telefonii a podporuje obchodní i osobní komunikační scénáře, kde je potřebné přesměrování hovoru. Přestože její využití pokleslo s nástupem IP služeb a aplikací na smartphonech, zůstává standardizovanou schopností v rámci 3GPP CS domény, což zajišťuje interoperabilitu a konzistentní chování služby napříč různými síťovými operátory a regiony.

## K čemu slouží

TTTP byla vytvořena, aby přinesla pokročilé telefonní funkce z pevného [ISDN](/mobilnisite/slovnik/isdn/) světa do mobilní domény a standardizovala je pro globální interoperabilitu. Před standardizací proprietární implementace nebo absence takových funkcí omezovaly kontrolu uživatele nad aktivními hovory. Problém, který řeší, je potřeba uživatele ručně spravovat scénář třístranného hovoru, kde je záměrem spojit dvě další strany a poté se sám odpojit – což je běžný požadavek v obchodním prostředí pro přenos hovorů na kolegy nebo oddělení.

Historicky, bez TTTP, by musel uživatel zavěsit a nechat jednu stranu zavolat druhé, nebo použít funkci konferenčního můstku a poté z ní vystoupit, což je méně efektivní a může být matoucí. TTTP poskytuje standardizovaný, síťově řízený postup, který je spolehlivý a účtovatelný. Její vytvoření bylo motivováno snahou nabídnout kompletní portfolio doplňkových služeb podobných ISDN v sítích GSM a UMTS, aby byla mobilní telefonie stejně funkčně bohatá jako její pevná linková obdoba a splňovala očekávání podnikových zákazníků.

Služba řeší omezení základního řízení hovoru tím, že poskytuje formalizovaný mechanismus pro přenos hovoru, který je bezproblémově integrován se síťovým účtováním a bezpečnostními mechanismy. Zajišťuje, že přenos je proveden správně sítí, při zachování kvality hovoru a poskytnutí odpovídající signalizace všem stranám. Přestože její relevance v éře VoLTE a [OTT](/mobilnisite/slovnik/ott/) komunikačních aplikací, které mohou podobnou funkcionalitu implementovat na aplikační vrstvě, poklesla, TTTP zůstává důležitou součástí legacy CS servisního rámce definovaného 3GPP.

## Klíčové vlastnosti

- Umožňuje přenos již navázaného aktivního hovoru na číslo třetí strany
- Síťová služba prováděná MSC na základě profilů předplacených v HLR
- Používá standardní signalizaci ISUP/BICC pro řízení hovoru mezi ústřednami
- Podporuje vyvolání pomocí DTMF tónů nebo flash-hook signálů od uživatele
- Poskytuje správné účtovací záznamy pro segmenty přenášejícího a přenášeného hovoru
- Integruje se s dalšími doplňkovými službami, jako je přidržení hovoru a čekání hovoru

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 29.172** (Rel-19) — EPC LCS Protocol (ELP) specification

---

📖 **Anglický originál a plná specifikace:** [TTTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tttp/)
