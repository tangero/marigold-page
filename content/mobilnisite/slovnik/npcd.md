---
slug: "npcd"
url: "/mobilnisite/slovnik/npcd/"
type: "slovnik"
title: "NPCD – Network Product Class Description"
date: 2025-01-01
abbr: "NPCD"
fullName: "Network Product Class Description"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/npcd/"
summary: "Podrobný dokument, který specifikuje bezpečnostní požadavky a hodnotící kritéria pro konkrétní třídu síťového produktu (Network Product Class, NPC). Definován v 3GPP TS 33.916, stanovuje přesné techni"
---

NPCD je závazný dokument 3GPP, který specifikuje přesné bezpečnostní požadavky a hodnotící kritéria, které musí produkt splnit, aby dosáhl určité klasifikace třídy síťového produktu (Network Product Class).

## Popis

Popis třídy síťového produktu (Network Product Class Description, NPCD) je klíčovou součástí rámce zajištění bezpečnosti 3GPP, formálně specifikovanou v TS 33.916. Jedná se o podrobný technický specifikační dokument, který definuje konkrétní třídu síťového produktu ([NPC](/mobilnisite/slovnik/npc/)). Pro každou odlišnou NPC (např. Třída 1, Třída 2) existuje odpovídající NPCD, který vyčerpávajícím způsobem uvádí bezpečnostní funkční požadavky, požadavky na zajištění bezpečnosti a hodnotící činnosti nezbytné k prokázání shody. Třídu NPC si lze představit jako označení (např. "IPC-A-610 Třída 3") a NPCD jako rozsáhlý, detailní normativní dokument, který definuje, co toto označení skutečně znamená z hlediska konkrétních testů, dokumentace a atributů návrhu.

Z hlediska architektury a provozu není NPCD běhovou komponentou, ale specifikací používanou během fází vývoje, hodnocení a pořizování. Funguje tak, že poskytuje jednoznačnou sadu kritérií. Dodavatel produktu, který usiluje o konkrétní NPC, musí navrhnout a vyrobit svůj produkt tak, aby splňoval každý příslušný požadavek v odpovídajícím NPCD. Nezávislé hodnotící laboratoře pak používají NPCD jako svůj testovací plán a kontrolní seznam pro ověření shody produktu. Dokument typicky obsahuje oddíly o definici bezpečnostního cíle, posouzení zranitelností, zabezpečení životního cyklu vývoje, testovacích metodikách a pokyny pro hodnocení bezpečnostních funkcí.

Jeho role v síťovém ekosystému je zásadní pro konzistentní měření úrovně bezpečnosti. NPCD zajišťuje, že všechny strany – dodavatelé, posuzovatelé a síťoví operátoři – sdílejí přesné, společné porozumění tomu, co daná bezpečnostní třída obnáší. Tím odstraňuje nejednoznačnost a subjektivní výklad. Kodifikací požadavků ve standardizovaném dokumentu umožňuje reprodukovatelné a srovnatelné bezpečnostní hodnocení napříč různými produkty a v čase. Existence dobře definovaných NPCD je tím, co dává rámci NPC jeho praktickou užitečnost a důvěryhodnost, přeměňujíc konceptuální klasifikaci v nástroj použitelný v inženýrské praxi a při pořizování.

## K čemu slouží

Popis třídy síťového produktu (Network Product Class Description, NPCD) byl vytvořen, aby řešil kritický problém nejednoznačnosti v bezpečnostních standardech. Zatímco koncept třídy síťového produktu ([NPC](/mobilnisite/slovnik/npc/)) stanovuje potřebu úrovní, bez přesné definice by pojem "Třída X" byl bezvýznamný. NPCD poskytuje potřebnou přesnost a detail, převádějící vysoké bezpečnostní cíle na konkrétní, ověřitelné požadavky. Jeho účelem je uvést rámec NPC do provozní praxe, učinit jej implementovatelným pro dodavatele a ověřitelným pro třetí strany.

Historicky bylo možné aplikovat obecné bezpečnostní standardy (jako Common Criteria), ty však vyžadovaly rozsáhlé přizpůsobení (Profily ochrany) pro telekomunikační kontext, což vedlo k nekonzistenci. NPCD je přímo určen pro produkty 3GPP sítí, přímo řeší jejich jedinečnou architekturu, rozhraní a prostředí hrozeb. Řeší problém, kdy operátoři od dodavatelů dostávají protichůdnou nebo neúplnou bezpečnostní dokumentaci, tím, že poskytuje jediný autoritativní zdroj pravdy o tom, co musí být prokázáno.

Motivací pro definování NPCD spolu s NPC bylo zajistit, aby rámec zajištění měl technickou hloubku a mohl skutečně zlepšovat bezpečnost produktů. Řeší omezení předchozích přístupů, kdy byly bezpečnostní tvrzení často spíše popisná než založená na důkazech. Vyžadováním konkrétních hodnotících činností a požadavků na důkazy NPCD posouvá paradigma směrem k objektivnímu, opakovatelnému ověřování, které je nezbytné pro budování důvěry ve složitých, více-dodavatelských dodavatelských řetězcích pro kritickou síťovou infrastrukturu.

## Klíčové vlastnosti

- Definuje přesné bezpečnostní funkční požadavky pro konkrétní NPC
- Specifikuje podrobné požadavky na zajištění bezpečnosti a hodnotící činnosti
- Slouží jako hlavní testovací plán pro certifikaci bezpečnosti produktu
- Poskytuje šablony pro požadovanou bezpečnostní dokumentaci (např. Bezpečnostní cíl)
- Zahrnuje pokyny pro posouzení zranitelností a testování průnikem
- Zajišťuje konzistentní výklad a aplikaci rámce NPC

## Související pojmy

- [NPC – Network Product Class](/mobilnisite/slovnik/npc/)

## Definující specifikace

- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [NPCD na 3GPP Explorer](https://3gpp-explorer.com/glossary/npcd/)
