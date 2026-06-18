---
slug: "ptch"
url: "/mobilnisite/slovnik/ptch/"
type: "slovnik"
title: "PTCH – Packet Traffic Channel"
date: 2025-01-01
abbr: "PTCH"
fullName: "Packet Traffic Channel"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ptch/"
summary: "Kanál PTCH (Packet Traffic Channel) je logický kanál v GSM/EDGE rádiové přístupové síti (GERAN) vyhrazený pro přenos datového provozu uživatele v paketovém režimu. Přepravuje vlastní užitečná data pro"
---

PTCH je logický kanál v GSM/EDGE rádiové přístupové síti (GERAN) vyhrazený pro přenos datového provozu uživatele, jako je prohlížení internetu, v paketovém režimu pro služby GPRS a EDGE.

## Popis

Kanál PTCH (Packet Traffic Channel) je základní přenosový kanál v uživatelské rovině v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)) pro paketově orientované služby. Jedná se o logický kanál, který přenáší zapouzdřené IP pakety nebo jiná data uživatele mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a sítí. Na rozdíl od kanálů pro přepojování okruhů, které jsou přiděleny na celou dobu hovoru, jsou prostředky PTCH dynamicky přidělovány a uvolňovány po jednotlivých blocích, což odráží trhavou povahu datového provozu. Tento kanál je hlavní pracovní silou pro datové služby [GPRS](/mobilnisite/slovnik/gprs/) a EDGE a přenáší vše od webových stránek po aplikační data.

Z architektonického hlediska je PTCH namapován na jeden nebo více fyzických paketových datových kanálů ([PDCH](/mobilnisite/slovnik/pdch/)). PDCH je fyzický GSM časový slot nakonfigurovaný pro přenos paketových dat. Jeden nebo více PTCH (přenášejících data pro různé uživatele nebo toky) může být pomocí statistického multiplexování sdíleno na jediném PDCH. Správu tohoto mapování a přidělování bloků konkrétním PTCH zajišťuje vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) v [BSC](/mobilnisite/slovnik/bsc/) a v MS. PTCH existuje v rámci tzv. dočasného blokového toku ([TBF](/mobilnisite/slovnik/tbf/)), což je dočasné logické spojení zřízené pro přenos sekvence datových bloků.

Provoz PTCH zahrnuje segmentaci protokolových datových jednotek (PDU) z vyšších vrstev na rádiové bloky vhodné pro přenos přes rozhraní vzduchu. Tyto bloky jsou vysílány v přidělených časových slotech v rámci struktury TDMA rámců. Síť řídí vysílání v uplinku pomocí příznaků stavu uplinku (USF) vysílaných na přidruženém paketovém asociovaném řídicím kanálu (PACCH), které udělují konkrétní MS oprávnění k odeslání dat na uplink PTCH. Vysílání v downlinku plánuje přímo síť. Každý blok obsahuje hlavičkové informace pro identifikaci a určení pořadí, což umožňuje přijímači znovusestavit původní PDU.

Role PTCH je klíčová pro uživatelský zážitek z datových služeb v sítích 2G a 2.5G. Jeho efektivita přímo ovlivňuje dosažitelnou datovou propustnost a latenci. Vylepšení jako EDGE zavedla nové modulační a kódovací schémy (MCS), které fungovaly na stejné struktuře PTCH/PDCH, a zvýšila tak špičkové datové rychlosti. Kanál podporuje jak potvrzovaný (pro spolehlivý přenos), tak nepotvrzovaný režim, čímž uspokojuje různé potřeby aplikací. Jeho konstrukční principy dynamického a sdíleného přidělování zdrojů položily základy pro paketově orientované kanály používané v pozdějších technologiích 3G (např. vyhrazený datový kanál (DTCH) v UMTS) a 4G.

## K čemu slouží

PTCH byl vytvořen, aby poskytoval nativní transportní mechanismus s přepojováním paketů v původně okruhově orientované architektuře GSM. Před GPRS mohlo GSM nabízet datové služby pouze prostřednictvím datových hovorů s přepojováním okruhů, které na celou dobu relace vyčlenily plný hovorový kanál – což byl pro trhavé, interaktivní datové aplikace neefektivní a drahý model. Hlavním důvodem byla potřeba efektivnější a nákladově výhodnější datové služby.

PTCH řeší problém efektivního využití rádiových zdrojů pro přerušovaný datový provoz. Tím, že umožňuje více uživatelům sdílet stejný fyzický časový slot (PDCH) a přiděluje rádiové bloky pouze v okamžiku, kdy jsou data připravena k odeslání, dramaticky zvyšuje spektrální účinnost ve srovnání s daty přepojovanými okruhy. Tento sdílený model na vyžádání učinil mobilní datové služby komerčně životaschopnými pro masový trh. Odstranil tak omezení vyplývající z vyhrazených, trvalých spojení, která byla plýtvavá pro typický start-stop charakter internetových protokolů.

Jeho zavedení v Rel-8 (v kontextu specifikací 3GPP pro správu) formalizovalo jeho roli v provozní a zpoplatňovací architektuře sítě. PTCH se stal klíčovou entitou pro měření objemu dat uživatele pro účely účtování a vynucování politik. Vytvoření PTCH jako samostatného typu logického kanálu umožnilo pokročilé řízení rádiových zdrojů, diferenciaci kvality služeb mezi uživateli a vývoj vylepšení EDGE, čímž zajistilo relevanci GSM v rané éře mobilního internetu.

## Klíčové vlastnosti

- Logický kanál vyhrazený pro přenos uživatelských paketových dat
- Dynamicky namapován na fyzické paketové datové kanály (PDCH)
- Funguje v rámci dočasného blokového toku (TBF) pro správu zdrojů
- Podporuje multiplexování více uživatelů/toků na sdílených zdrojích PDCH
- Využívá příznaky stavu uplinku (USF) pro řízený přístup v uplinku
- Podporuje jak potvrzovaný, tak nepotvrzovaný režim provozu

## Související pojmy

- [PDCH – Packet Data Channel](/mobilnisite/slovnik/pdch/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [PACCH – Packet Associated Control Channel](/mobilnisite/slovnik/pacch/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [PTCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptch/)
