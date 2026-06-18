---
slug: "pbsp"
url: "/mobilnisite/slovnik/pbsp/"
type: "slovnik"
title: "PBSP – Personal Broadcast Service Provider"
date: 2025-01-01
abbr: "PBSP"
fullName: "Personal Broadcast Service Provider"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pbsp/"
summary: "Personal Broadcast Service Provider (PBSP) je entita poskytovatele služeb podle 3GPP odpovědná za vytváření, správu a doručování personalizovaného vysílacího obsahu mobilním uživatelům. Umožňuje předp"
---

PBSP je entita poskytovatele služeb podle 3GPP odpovědná za vytváření, správu a doručování personalizovaného vysílacího obsahu mobilním uživatelům.

## Popis

Personal Broadcast Service Provider (PBSP) je funkční entita definovaná v rámci architektury služeb 3GPP, konkrétně pro službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Funguje jako komponenta vrstvy služeb, která komunikuje s Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) a dalšími prvky jádra sítě. PBSP je zodpovědný za komplexní správu personalizovaných vysílacích služeb, včetně vytváření služeb, poskytování obsahu, správy účastníků a vynucování pravidel pro doručování.

Z architektonického hlediska PBSP komunikuje s BM-SC, které slouží jako vstupní bod pro vysílací obsah do sítě 3GPP. PBSP poskytuje BM-SC informace specifické pro službu, jako jsou uživatelské profilové údaje předplatitele, pravidla pro personalizaci obsahu a zásady účtování. To umožňuje BM-SC přizpůsobit vysílací relaci. PBSP může také komunikovat s externími poskytovateli obsahu a s Home Subscriber System ([HSS](/mobilnisite/slovnik/hss/)) za účelem autentizace uživatelů a získání dat o předplatném.

Klíčové součásti funkčnosti PBSP zahrnují modul správy služeb pro definování a konfiguraci vysílacích služeb, modul správy účastníků pro zpracování uživatelských profilů a oprávnění, modul správy obsahu pro organizaci a personalizaci mediálních dat a modul správy politik pro vynucování pravidel doručování na základě podmínek uživatele, sítě a služby. PBSP hraje klíčovou roli při umožnění komerčních vysílacích služeb díky podpoře modelů předplatného, cílené reklamy a diferencované kvality služby.

Jeho provoz zahrnuje definování oblasti služby, plánování vysílacích relací a přidružení metadat služby k obsahu. Když uživatel požaduje personalizovanou vysílací službu, PBSP ověří předplatné, určí příslušnou variantu obsahu nebo doplňková data a dá pokyn BM-SC k odpovídajícímu zahájení nebo úpravě vysílacího přenosu. To umožňuje scénáře, kde může být jediný vysílací proud doplněn personalizovanými daty doručovanými jednotlivým zařízením jednosměrným přenosem, čímž vzniká hybridní model doručování.

## K čemu slouží

PBSP byl zaveden, aby řešil potřebu komerčních a personalizovaných vysílacích služeb v mobilních sítích, což znamená posun od jednoduchého, jednotného vysílání pro všechny. Před jeho specifikací [MBMS](/mobilnisite/slovnik/mbms/) primárně podporovalo anonymní, nepersonalizované doručování obsahu, jako je mobilní televize, což omezovalo modely výnosů na reklamu nebo paušální přístup. Vytvoření entity PBSP bylo motivováno snahou umožnit služby založené na předplatném, doručování prémiového obsahu a přizpůsobení služeb konkrétnímu uživateli.

Řeší problém, jak efektivně doručit stejný multimediální obsah mnoha uživatelům, a přitom zachovat možnost personalizace, jako je cílená reklama, výběr jazyka nebo interaktivní vylepšení. Tento hybridní přístup kombinuje spektrální efektivitu vysílání s možnostmi přizpůsobení jednosměrného přenosu. PBSP poskytuje nezbytnou logiku vrstvy služeb pro správu uživatelských identit, oprávnění a personalizačních pravidel v kontextu vysílání, což nebylo v dřívějších architekturách MBMS nativně podporováno.

Historický kontext představuje vývoj MBMS z technologicky orientované funkce na komerčně životaschopnou platformu služeb. Operátoři a poskytovatelé obsahu hledali způsoby, jak monetizovat vysílací sítě prostřednictvím vrstvených předplatných, placených událostí a personalizované reklamy. PBSP standardizuje role a rozhraní potřebné pro takové služby, zajišťuje interoperabilitu mezi servisními platformami a síťovými zařízeními různých dodavatelů, a tím podporuje ekosystém pro personalizované mobilní vysílání.

## Klíčové vlastnosti

- Spravuje předplatné a oprávnění pro personalizované vysílací služby
- Komunikuje s BM-SC za účelem poskytování informací o službě a zásadách
- Podporuje hybridní doručování kombinující vysílání a jednosměrný přenos pro personalizaci
- Umožňuje účtování založené na službě a komerční modely pro MBMS
- Umožňuje definici oblastí služby a plánování vysílacích relací
- Usnadňuje cílené vkládání obsahu a uživatelsky specifická metadata

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TR 22.947** (Rel-19) — Personal Broadcast Service (PBS) Use Cases

---

📖 **Anglický originál a plná specifikace:** [PBSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbsp/)
