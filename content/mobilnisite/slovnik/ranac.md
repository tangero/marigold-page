---
slug: "ranac"
url: "/mobilnisite/slovnik/ranac/"
type: "slovnik"
title: "RANAC – RAN-based Notification Area Code"
date: 2025-01-01
abbr: "RANAC"
fullName: "RAN-based Notification Area Code"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ranac/"
summary: "RAN-based Notification Area Code (RANAC) je identifikátor používaný v 5G k definování oblasti pro oznamování na bázi RAN (RNA) pro uživatelská zařízení (UE) ve stavu RRC_INACTIVE. Umožňuje RAN efektiv"
---

RANAC je identifikátor používaný v 5G k definování oblasti pro oznamování na bázi RAN (RAN-based Notification Area) pro efektivní vyhledávání a lokalizaci neaktivních uživatelských zařízení (UE) v rámci konkrétní oblasti, což snižuje signalizační režii.

## Popis

Kód oblasti pro oznamování na bázi RAN (RANAC) je základní součástí správy mobility pro stav [RRC](/mobilnisite/slovnik/rrc/)_INACTIVE v 5G New Radio (NR). Oblast pro oznamování na bázi RAN ([RNA](/mobilnisite/slovnik/rna/)) je logická oblast, složená z jedné nebo více buněk, definovaná RAN za účelem sledování a vyhledávání uživatelského zařízení (UE), které je ve stavu RRC_INACTIVE. RANAC je kód, který tuto RNA jednoznačně identifikuje v rámci působnosti gNodeB nebo skupiny gNodeB. Když UE přejde do stavu RRC_INACTIVE, síť mu přiřadí RNA a UE uloží odpovídající RANAC.

Fungování se točí kolem mobility UE v rámci této RNA. Zatímco je ve stavu RRC_INACTIVE, se může UE volně pohybovat v rámci buněk, které patří k jeho přiřazené RNA, aniž by o tom informovalo síť, čímž šetří energii baterie a snižuje signalizaci. UE provádí periodické aktualizace RNA ([RNAU](/mobilnisite/slovnik/rnau/)) nebo je k provedení takové aktualizace vyvoláno, když se přesune do buňky, která je mimo jeho současnou RNA. Během tohoto procesu RNAU poskytne UE nové buňce svůj poslední uložený RANAC a další kontextové informace, což umožní RAN načíst kontext UE z předchozí obsluhující gNodeB a aktualizovat jeho polohu.

Když pro UE ve stavu RRC_INACTIVE dorazí datový provoz ve směru downlink, RAN zahájí proceduru vyhledávání na bázi RAN v rámci poslední známé RNA daného UE. gNodeB v této RNA vysílají broadcastem zprávu pro vyhledávání obsahující identifikátor UE a příslušný RANAC. UE, které monitoruje zprávy pro vyhledávání ve své aktuální buňce, odpoví, pokud se nachází v oblasti, kde je vyhledáváno. Tento mechanismus je efektivnější než vyhledávání na úrovni jádra sítě (prostřednictvím 5GC) pro neaktivní UE, protože lokalizuje provoz spojený s vyhledáváním do menší oblasti definované RAN. RANAC je tedy klíčovým prvkem pro efektivní správu stavů, vyvažujícím kompromis mezi signalizační režií a spotřebou energie UE, což je zvláště důležité pro komunikaci typu massive Machine-Type Communication (mMTC) a běžné uživatele mobilního širokopásmového připojení.

## K čemu slouží

RANAC byl vytvořen, aby řešil výzvy v oblasti efektivity signalizace a spotřeby energie spojené se správou obrovského počtu připojených zařízení, zejména pro scénáře IoT, v 5G sítích. Předchozí stavy, jako [RRC](/mobilnisite/slovnik/rrc/)_IDLE v LTE, vyžadovaly zapojení jádra sítě ([MME](/mobilnisite/slovnik/mme/)) pro aktualizace oblasti sledování a vyhledávání, což mohlo generovat významnou signalizační zátěž. Stav RRC_CONNECTED, i když udržuje kontext UE v RAN, spotřebovává více energie z baterie UE, protože je udržováno rádiové spojení. Nový stav RRC_INACTIVE a s ním spojený koncept [RNA](/mobilnisite/slovnik/rna/) identifikovaný pomocí RANAC představuje střední cestu.

Primární problém, který RANAC řeší, je umožnění efektivního sledování polohy a vyhledávání pro UE, která jsou neaktivní, ale jejichž datové relace mohou být brzy obnoveny. Definováním RNA spravované výhradně RAN nezatěžují aktualizace polohy (RNA Updates) jádro 5G sítě (5GC), pokud se UE nepřesune mimo oblast řízenou RAN. Tím se snižuje signalizace na rozhraní [N2](/mobilnisite/slovnik/n2/) mezi RAN a [AMF](/mobilnisite/slovnik/amf/). Dále vyhledávání na bázi RAN využívající RANAC omezuje zprávy pro vyhledávání na konkrétní skupinu buněk, čímž snižuje zbytečnou zátěž vyhledávání v celé oblasti sledování a umožňuje rychlejší obnovení spojení.

Tato inovace byla motivována požadavkem 5G podporovat masivní nasazení IoT s miliardami zařízení, která přenášejí data sporadicky. Pro taková zařízení je minimalizace signalizace a spotřeby energie prvořadá. RANAC jako součást mechanismu RNA umožňuje těmto zařízením zůstat pro síť dosažitelná s minimálními energetickými náklady, což prodlužuje výdrž baterie na roky, a zároveň zajišťuje, že síť může při potřebě efektivně doručit příchozí data, naplňujíc tak sliby 5G mMTC a zvýšené efektivity mobilního širokopásmového připojení.

## Klíčové vlastnosti

- Jednoznačně identifikuje oblast pro oznamování na bázi RAN (RNA) v rámci 5G NR
- Umožňuje mobilitu UE v rámci RNA bez signalizace (výběr buňky – cell reselection)
- Spouští proceduru aktualizace RNA (RNAU), když se UE přesune mimo svou současnou RNA
- Používá se při vyhledávání na bázi RAN k lokalizaci UE ve stavu RRC_INACTIVE
- Snižuje signalizaci směrem k jádru 5G sítě (5GC) pro neaktivní UE
- Kritický pro provoz s úsporou energie u IoT a mobilních zařízení ve stavu RRC_INACTIVE

## Související pojmy

- [RNA – RAN-based Notification Area](/mobilnisite/slovnik/rna/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 37.473** (Rel-19) — W1 Application Protocol (W1AP) Specification
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- **TS 38.463** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [RANAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ranac/)
