---
slug: "mfn"
url: "/mobilnisite/slovnik/mfn/"
type: "slovnik"
title: "MFN – Multicast Frame Number"
date: 2025-01-01
abbr: "MFN"
fullName: "Multicast Frame Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mfn/"
summary: "Čítač používaný ve standardu 3GPP UMTS pro synchronizaci a řazení multicastových datových přenosů přes rozhraní rádiového přístupu. Zajišťuje spolehlivé doručování a správné pořadí multicastových pake"
---

MFN je čítač používaný ve standardu 3GPP UMTS pro synchronizaci a řazení multicastových datových přenosů, který poskytuje časovou referenci pro spolehlivé doručování služby MBMS přes rozhraní rádiového přístupu.

## Popis

Multicast Frame Number (MFN) je základní časový a synchronizační mechanismus definovaný v architektuře rádiové přístupové sítě UMTS (UTRAN) dle 3GPP, konkrétně pro operace služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Funguje jako cyklický čítač, jehož hodnota se zvyšuje s každým rádiovým rámcem vysílaným na transportním kanálu MBMS ([MTCH](/mobilnisite/slovnik/mtch/)). Hodnotu MFN vysílá Node B (základnová stanice) jako součást systémové informace, což umožňuje všem uživatelským zařízením (UE) v oblasti pokrytí služby MBMS sladit časování příjmu. Toto sladění je klíčové, protože MBMS je služba typu point-to-multipoint, kde je jeden přenos určen pro více přijímačů současně; bez společné časové reference by měla UE potíže se správným sestavením datových bloků a udržením synchronizace, což by vedlo k chybám příjmu a degradaci služby.

Z architektonického hlediska je MFN generován a spravován v řadiči rádiové sítě (RNC), který je zodpovědný za plánování přenosů MBMS. RNC přiřazuje hodnotu MFN pro každou MBMS relaci a sděluje ji Node B přes rozhraní Iub pomocí signalizace [NBAP](/mobilnisite/slovnik/nbap/) (Node B Application Part), jak je podrobně popsáno ve specifikaci 25.433. Node B následně začlení MFN do fyzického rámcování vysílacího kanálu. Z perspektivy protokolového zásobníku je MFN asociován s vrstvou [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control) a fyzickou vrstvou, čímž vytváří vazbu mezi plánováním prováděným v RNC a samotným rádiovým přenosem. Umožňuje MAC vrstvě UE identifikovat začátek přenosových období MBMS a správně ukládat do vyrovnávací paměti a řadit datové bloky přijaté přes potenciálně nespolehlivá rádiová spojení.

Během provozu MFN umožňuje síti implementovat časový multiplex různých služeb MBMS na sdílených rádiových zdrojích. RNC může naplánovat vysílání různých služeb v konkrétních rámcích identifikovaných jejich MFN, což umožňuje efektivní využití spektra. Pro UE je znalost MFN zásadní pro procedury jako je počítání (zjistění, kolik UE má zájem o službu) a pro nespojitý příjem ([DRX](/mobilnisite/slovnik/drx/)), kdy může UE vypnout svůj přijímač během rámců, které neobsahují požadovanou službu, a tím šetřit životnost baterie. MFN tedy není jen prostým čítačem, ale klíčovým prvkem umožňujícím koordinované, efektivní a spolehlivé doručování broadcastového a multicastového obsahu v sítích UMTS.

## K čemu slouží

MFN byl zaveden, aby vyřešil zásadní výzvu synchronizace přenosu dat typu one-to-many v mobilní síti. Před službou [MBMS](/mobilnisite/slovnik/mbms/) byly mobilní protokoly optimalizovány pro spojení point-to-point (unicast), kde se časování mohlo řídit pomocí vyhrazené signalizace s každým UE. Broadcast/multicast ze své podstaty tento vyhrazený zpětnovazební okruh pro synchronizaci s každým přijímačem postrádá. MFN poskytuje společnou, síťově řízenou časovou referenci, kterou mohou všechna naslouchající UE nezávisle používat pro sladění svého příjmu. Tato inovace byla nezbytná, aby se efektivní hromadné doručování obsahu (jako mobilní TV nebo aktualizace softwaru) stalo technicky proveditelným přes UMTS.

Jeho vytvoření bylo přímo motivováno vývojem funkce Multimedia Broadcast Multicast Service (MBMS) ve 3GPP Release 6. MBMS mělo za cíl umožnit operátorům nabízet broadcastové služby, ale vyžadovalo nové mechanismy v rádiovém rozhraní pro zvládnutí jedinečných charakteristik broadcastu. MFN řešil konkrétní problém plánování přenosů a časového sladění UE bez nutnosti individuální signalizace ke každému UE, což by bylo pro broadcastové publikum neškálovatelné. Poskytl časovou strukturu potřebnou k tomu, aby UE vědělo, *kdy* má naslouchat konkrétním službám, což umožnilo režimy šetřící energii a spolehlivé sestavování dat.

## Klíčové vlastnosti

- Poskytuje společnou cyklickou časovou referenci pro všechna UE přijímající službu MBMS
- Umožňuje časový multiplex více služeb MBMS na sdílených rádiových zdrojích
- Usnadňuje procedury UE pro nespojitý příjem (DRX) za účelem úspory energie baterie
- Podporuje synchronizaci pro procedury počítání za účelem zjištění zájmu o službu
- Vysílán jako součást systémové informace, nevyžaduje vyhrazenou signalizaci na každé UE
- Spravován RNC a vysílán přes Node B na fyzické vrstvě

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)
- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)

## Definující specifikace

- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols

---

📖 **Anglický originál a plná specifikace:** [MFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/mfn/)
