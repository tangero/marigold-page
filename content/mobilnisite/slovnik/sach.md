---
slug: "sach"
url: "/mobilnisite/slovnik/sach/"
type: "slovnik"
title: "SACH – Service Announcement CHannel"
date: 2025-01-01
abbr: "SACH"
fullName: "Service Announcement CHannel"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sach/"
summary: "Kanál používaný k vysílání informací o dostupnosti služeb a konfiguraci zařízením v síti 3GPP. Umožňuje efektivní objevování a přístup ke službám, jako je Multimedia Broadcast/Multicast Service (MBMS)"
---

SACH je vysílací kanál používaný v sítích 3GPP pro oznamování dostupnosti služeb a konfiguračních informací, který umožňuje efektivní objevování zařízení a přístup ke službám, jako je MBMS.

## Popis

Service Announcement CHannel (SACH) je logický kanál definovaný v rámci architektury služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) konsorcia 3GPP. Jeho primární funkcí je distribuovat oznámení o službách, což jsou metadata popisující dostupné služby MBMS, k uživatelským zařízením (UE) v rámci vysílací oblasti. Tato oznámení obsahují klíčové informace, jako jsou identifikátory služeb, časy začátku relací, popisy médií a přístupové parametry, což umožňuje zařízením objevit a následně se připojit k požadovaným vysílacím nebo skupinovým relacím.

Z architektonického hlediska SACH funguje jako součást přenosové služby MBMS. Broadcast Multicast Service Centre ([BM-SC](/mobilnisite/slovnik/bm-sc/)), hlavní síťová entita zodpovědná za poskytování služeb MBMS, generuje informace pro oznámení služeb. Tyto informace jsou následně doručovány přes přenos MBMS do rádiové přístupové sítě (např. LTE nebo 5G NR). Síť vysílá data SACH v rámci specifických oblastí služby MBMS pomocí přenosu typu point-to-multipoint. Kanál je typicky přenášen přes protokoly řídicí roviny, což zajišťuje jeho dostupnost všem zařízením UE schopným příjmu MBMS, a to i těm, která ještě aktivně nekonzumují mediální stream.

Technická operace zahrnuje sestavení protokolové zprávy Service Announcement ([SA](/mobilnisite/slovnik/sa/)) entitou BM-SC. Tato zpráva je formátována podle specifikací (např. s použitím [XML](/mobilnisite/slovnik/xml/) nebo binárního kódování definovaného ve specifikacích) a obsahuje seznam dostupných služeb MBMS. Síť plánuje vysílání těchto zpráv SACH, často periodicky, aby zajistila, že zařízení mohou přijímat aktualizace. Když zařízení UE vstoupí do oblasti služby MBMS nebo si přeje objevit služby, naslouchá vysílání SACH. Po přijetí oznámení o službě, ke které se chce připojit, zařízení extrahuje potřebné informace o relaci, jako je Temporary Mobile Group Identity ([TMGI](/mobilnisite/slovnik/tmgi/)) a načasování relace, které pak použije ke konfiguraci svého přijímače pro připojení k odpovídajícímu datovému přenosu MBMS.

SACH hraje klíčovou roli v ekosystému MBMS tím, že odděluje objevování služeb od doručování médií. Optimalizuje síťové a zařízení zdroje tím, že zabraňuje potřebě, aby zařízení jednotlivě dotazovala server o seznamy služeb, což by generovalo významný provoz v uplinku a zatížení zpracováním. Místo toho jediné efektivní vysílání obslouží všechna zařízení v oblasti. Je základním kamenem pro služby jako evolved MBMS (eMBMS) a jeho vylepšení v 5G, podporující aplikace od varovných systémů pro veřejnou bezpečnost až po mobilní [TV](/mobilnisite/slovnik/tv/).

## K čemu slouží

Service Announcement CHannel byl zaveden k řešení problému škálovatelného a efektivního objevování služeb pro vysílací a skupinové služby v mobilních sítích. Před [MBMS](/mobilnisite/slovnik/mbms/) a SACH se doručování identického obsahu mnoha uživatelům často spoléhalo na jednotlivé unicastové streamy, což plýtvalo síťovou kapacitou při vysoké popularitě. Rané koncepty multicastu postrádaly standardizovanou, efektivní metodu, jak se zařízení mohou dozvědět, jaké vysílací služby jsou na jejich aktuálním místě dostupné a jak k nim získat přístup.

SACH byl vytvořen jako součást širší architektury MBMS, aby umožnil doručování obsahu typu one-to-many. Jeho specifickým účelem je poskytnout standardizovaný, síťově řízený kanál pro vysílání metadat služeb. Tím se řeší omezení, kdy by zařízení jinak musela používat unicastová spojení (např. [HTTP](/mobilnisite/slovnik/http/) dotazy) na servisní portál, což generuje redundantní provoz a zpoždění, zejména když tisíce zařízení v buňce hledají stejné informace. Vysíláním těchto dat SACH snižuje zatížení uplinku, šetří baterii zařízení a urychluje objevování služeb.

Historický kontext je spojen s vývojem eMBMS v LTE (od Rel-9 dále) a jeho zdokonalením v pozdějších vydáních. SACH, formalizovaný v Rel-13, se stal nedílnou součástí pokročilých případů užití MBMS, jako jsou systémy varování pro veřejnost, zážitky na akcích a automobilové aplikace. Poskytuje nezbytnou vrstvu řídicích informací, která činí MBMS praktickou a uživatelsky přívětivou službou, posouvá se tak od pouhého doručování dat k řízenému přístupu ke službám a uživatelskému zážitku.

## Klíčové vlastnosti

- Vysílá metadata pro dostupné služby MBMS (např. ID služby, čas relace, typ média)
- Používá přenos typu point-to-multipoint pro efektivní doručení všem zařízením UE v oblasti
- Přenášen přes řídicí přenosy MBMS, odděleně od datových přenosů pro média
- Umožňuje zařízením UE objevovat služby bez nutnosti jednotlivých unicastových dotazů
- Podporuje periodické a na požádání aktualizace oznámení
- Obsahuje parametry pro připojení zařízení UE k relaci (TMGI, IP multicastová adresa)

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [TMGI – Temporary Multicast Group Identifier](/mobilnisite/slovnik/tmgi/)

## Definující specifikace

- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TR 26.981** (Rel-19) — MBMS Provisioning & Content Ingestion Interface Study
- **TS 29.116** (Rel-19) — REST-based protocol for xMB reference point
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs

---

📖 **Anglický originál a plná specifikace:** [SACH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sach/)
