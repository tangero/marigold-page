---
slug: "lle"
url: "/mobilnisite/slovnik/lle/"
type: "slovnik"
title: "LLE – Logical Link Entity"
date: 2025-01-01
abbr: "LLE"
fullName: "Logical Link Entity"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lle/"
summary: "LLE je konceptuální entita ve vrstvě logického spojení (Logical Link Control) GPRS, která reprezentuje instanci logického spoje mezi mobilní stanicí a sítí. Spravuje stav, parametry a tok dat pro konk"
---

LLE je konceptuální entita ve vrstvě logického spojení (Logical Link Control) GPRS, která reprezentuje a spravuje stav, parametry a tok dat logického spoje mezi mobilní stanicí a sítí.

## Popis

Logical Link Entity (LLE) je funkční komponenta v implementaci protokolu vrstvy logického spojení (Logical Link Control – [LLC](/mobilnisite/slovnik/llc/)), jak je definována ve specifikacích 3GPP, zejména pro [GPRS](/mobilnisite/slovnik/gprs/). Reprezentuje instanci logického spoje mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a podpůrným uzlem [SGSN](/mobilnisite/slovnik/sgsn/) (Serving GPRS Support Node). Každá LLE odpovídá konkrétnímu logickému spoji identifikovanému identifikátorem datového spojení (Data Link Connection Identifier – [DLCI](/mobilnisite/slovnik/dlci/)) a je asociována s konkrétním bodem přístupu ke službě (Service Access Point – [SAP](/mobilnisite/slovnik/sap/)), jako jsou ty používané pro uživatelská data (LLC-SAPI) nebo signalizaci správy mobility GPRS (LLGMM-SAPI). LLE spravuje úplný stavový automat, kontext a provozní parametry pro daný logický spoj.

Interně LLE udržuje proměnné jako vysílací a přijímací stavové proměnné (V(S), V(R), V(A)) pro číslování sekvencí v potvrzovaném režimu, čítač retransmisí, časovače pro potvrzení a retransmise, stav šifrování a klíč a vyrovnávací paměti pro vyslané a přijaté LLC rámce. Provádí procedury protokolu LLC, včetně vysílání a příjmu rámců, detekce chyb, operací [ARQ](/mobilnisite/slovnik/arq/) pro retransmise, řízení toku a šifrování/dešifrování. Pro každý aktivní [PDP](/mobilnisite/slovnik/pdp/) kontext nebo signalizační spojení je typicky vytvořena samostatná LLE pro obsluhu jeho datového toku, což umožňuje souběžný provoz více logických spojů na stejném fyzickém rádiovém prostředku.

LLE komunikuje s přilehlými vrstvami: přijímá datové jednotky služby (SDUs) z vyšší vrstvy (např. SNDCP pro uživatelská data nebo GMM pro signalizaci) prostřednictvím SAP, segmentuje je na LLC datové jednotky protokolu (PDUs) a předává je nižší vrstvě RLC/MAC pro přenos přes rozhraní rádiového přístupu. V opačném směru přijímá LLC PDUs z RLC/MAC, znovu je skládá do SDUs a doručuje je příslušné entitě vyšší vrstvy. Stavový automat LLE obsluhuje procedury navázání spoje (prostřednictvím výměny XID), přenosu dat a uvolnění spoje. Na straně sítě (SGSN) existuje LLE pro každou mobilní stanici a každý aktivní logický spoj, která spravuje peer-to-peer spojení s odpovídající LLE na straně MS.

## K čemu slouží

Koncept Logical Link Entity byl formálně podrobně popsán v pozdějších vydáních 3GPP, jako je Release 8, aby poskytl jasný architektonický model pro implementaci vrstvy LLC. Řeší potřebu spravovat více nezávislých logických spojení přes jediný fyzický rádiový spoj mezi mobilní stanicí a sítí. Bez oddělených entit logického spoje by bylo obtížné podporovat simultánní služby, jako je prohlížení webu, e-mail a signalizace mobility, z nichž každá může mít odlišné požadavky na spolehlivost a QoS.

Jeho zavedení vychází z požadavku na strukturovaný způsob správy stavu a kontextu spojeného s každým logickým spojem. Starší specifikace GPRS definovaly procedury LLC, ale byly méně explicitní ohledně vnitřní struktury. Model LLE pomáhá výrobcům zařízení a vývojářům protokolových zásobníků tím, že definuje modulární entitu, která zapouzdřuje všechny funkce související s konkrétním logickým spojem. To zlepšuje softwarový návrh, testování a interoperabilitu.

LLE řeší problém správy kontextu během událostí mobility, jako jsou předávání spojení nebo aktualizace směrovací oblasti. Protože je stav každého logického spoje (sekvenční čísla, šifrovací klíče, vyrovnávací paměti) udržován v jeho vlastní LLE, může síť tyto kontexty efektivně pozastavit, obnovit nebo přenést mezi síťovými uzly (např. při předávání mezi SGSN). To zajišťuje kontinuitu služby a efektivní využití prostředků, což je klíčové pro plynulý zážitek z mobilních dat.

## Klíčové vlastnosti

- Spravuje stavový automat a kontext pro jeden logický spoj
- Zpracovává číslování sekvencí a ARQ pro spolehlivý přenos
- Udržuje parametry šifrování a provádí šifrování/dešifrování
- Ukládá LLC rámce do vyrovnávací paměti pro přenos a retransmise
- Komunikuje s vyššími vrstvami prostřednictvím bodů přístupu ke službě (SAPs)
- Podporuje souběžný provoz více LLE na jednu mobilní stanici

## Související pojmy

- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)
- [LLGMM – LLC to GPRS Mobility Management service access point](/mobilnisite/slovnik/llgmm/)
- [SAPI – Service Access Point Identifier](/mobilnisite/slovnik/sapi/)
- [DLCI – Data Link Connection Identifier](/mobilnisite/slovnik/dlci/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [LLE na 3GPP Explorer](https://3gpp-explorer.com/glossary/lle/)
