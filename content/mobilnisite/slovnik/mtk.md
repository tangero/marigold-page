---
slug: "mtk"
url: "/mobilnisite/slovnik/mtk/"
type: "slovnik"
title: "MTK – MBMS Traffic Key"
date: 2025-01-01
abbr: "MTK"
fullName: "MBMS Traffic Key"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mtk/"
summary: "MBMS Traffic Key (MTK) je kryptografický klíč používaný k šifrování vysílaného a multicastového provozu v systémech Multimedia Broadcast Multicast Service (MBMS). Zajišťuje důvěrnost a integritu obsah"
---

MTK je kryptografický klíč používaný k šifrování vysílaného a multicastového provozu v systémech MBMS, který zajišťuje důvěrnost a integritu obsahu doručovaného více uživatelům současně.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) Traffic Key (MTK) je základní bezpečnostní komponenta v architektuře služby Multimedia Broadcast Multicast Service (MBMS) podle 3GPP, speciálně navržená pro zabezpečení doručování obsahu typu point-to-multipoint. Funguje jako symetrický šifrovací klíč, což znamená, že stejný klíč používá síť k zašifrování vysílacího provozu a autorizované uživatelské zařízení (UE) k jeho dešifrování. MTK se aplikuje na aplikační vrstvě, typicky v rámci MBMS User Service vrstvy nebo v Broadcast Multicast Service Centre ([BM-SC](/mobilnisite/slovnik/bm-sc/)), aby chránil vlastní mediální obsah, jako jsou video streamy, stahování souborů nebo datová vysílání. Jeho primární rolí je zajistit, aby obsah mohl přistupovat pouze účastníci oprávnění přijímat konkrétní službu MBMS, čímž vynucuje důvěrnost na úrovni služby.

Generování, distribuce a správa MTK jsou řízeny bezpečnostním rámcem MBMS definovaným ve specifikacích 3GPP. Klíč generuje BM-SC, který funguje jako servisní a bezpečnostní kotva pro MBMS. MTK není přímo přenášen vzduchem k UE v nezašifrované podobě. Místo toho je bezpečně doručen pomocí hierarchie klíčů. Samotný MTK je zašifrován pomocí jiného klíče, MBMS Service Key ([MSK](/mobilnisite/slovnik/msk/)), který je jedinečně zřízen každému odebírajícímu UE nebo skupině UE. Tento zašifrovaný MTK spolu s dalšími servisními metadaty je distribuován prostřednictvím MBMS User Service Description (USD) nebo podobných mechanismů oznamování služby. Když si UE přeje přistoupit k službě MBMS, použije svůj předem zřízený MSK k dešifrování přijatého MTK. Po dešifrování UE MTK lokálně uloží a používá jej k dešifrování příchozího vysílacího provozu po dobu platnosti klíče nebo relace služby.

Životní cyklus MTK zahrnuje generování, aktivaci, používání a expiraci nebo obnovu. Pro udržení bezpečnosti jsou MTK typicky měněny periodicky (např. na relaci služby, na položku obsahu nebo v časových intervalech), aby se omezil dopad případného kompromitování klíče. Specifikace podrobně popisují procedury obnovy klíče, kdy je vygenerován a distribuován nový MTK, často před expirací starého klíče, aby bylo umožněno plynulé pokračování služby. Celý proces je navržen jako škálovatelný pro hromadné doručování, protože stejný MTK může používat miliony zařízení přijímajících stejné vysílání, zatímco individuální MSK poskytuje personalizovaný řízení přístupu. Integrita zpráv distribuce klíčů je také chráněna, často prostřednictvím digitálních podpisů od BM-SC, aby se zabránilo manipulaci.

V rámci širší architektury MBMS MTK spolupracuje s dalšími klíči, jako jsou MSK a [MUK](/mobilnisite/slovnik/muk/) (MBMS User Key). BM-SC používá rozhraní Gi/Sgi-mb pro poskytování služeb a rozhraní Gmb pro signalizaci s jádrem sítě. Zašifrovaný provoz teče z BM-SC přes jádro sítě (např. přes MBMS Gateway) k rádiové přístupové síti (např. k [eNB](/mobilnisite/slovnik/enb/) nebo gNB v LTE/5G) pro vysílání přes oblast Multicast-Broadcast Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)). MBMS klient v UE po úspěšném ověření a odvození klíčů získá přístup k MTK a nakonfiguruje svůj dešifrovací engine ke zpracování přijatých vysílacích paketů. Tento mechanismus je klíčový pro komerční služby jako mobilní TV, výstrahy pro veřejnou bezpečnost a bezdrátové aktualizace softwaru, kde je ochrana obsahu povinným požadavkem.

## K čemu slouží

[MBMS](/mobilnisite/slovnik/mbms/) Traffic Key byl zaveden, aby řešil kritickou potřebu zabezpečení vysílaného a multicastového obsahu v mobilních sítích. Před MBMS bylo doručování unicast bezpečné, ale pro oblíbený obsah určený mnoha uživatelům neefektivní, protože spotřebovávalo nadměrné síťové zdroje. Jednoduché vysílání bez šifrování, používané v některých starších technologiích, postrádalo jakoukoli ochranu obsahu, což jej činilo nevhodným pro prémiové nebo privátní služby. MTK umožňuje efektivní doručování obsahu ve velkém měřítku a zároveň zavádí robustní bezpečnostní vrstvu, která dříve ve vysílacích scénářích chyběla nebo byla nedostatečná.

Vytvoření MTK bylo motivováno komerčním nasazením služby Multimedia Broadcast Multicast Service (MBMS), počínaje 3GPP Release 6, které si kladlo za cíl umožnit služby jako mobilní televize, skupinová komunikace a distribuce souborů. Poskytovatelé služeb a vlastníci obsahu požadovali záruky, že vysílací streamy budou moci přistupovat pouze platící účastníci, čímž se zabrání ztrátám příjmů z pirátství. Dále pro aplikace veřejné bezpečnosti a podnikové sféry je prvořadé zajistit, aby citlivé vysílané informace (např. výstrahy při mimořádných událostech) přijímali pouze autorizovaný personál. MTK jako součást standardizované hierarchie správy klíčů poskytl škálovatelné řešení těchto požadavků.

Řeší problém, jak efektivně spravovat šifrovací klíče pro potenciálně miliony současných příjemců. Distribuce unikátních klíčů každému zařízení pro samotný provoz by byla nepraktická. Koncepce MTK jako společného klíče pro provoz, chráněného individuálně přiřazenými servisními klíči ([MSK](/mobilnisite/slovnik/msk/)), elegantně vyvažuje škálovatelnost a bezpečnost. Tento přístup omezuje vystavení kritického MTK, protože je vždy přenášen v zašifrované formě, a umožňuje periodické aktualizace klíčů ke zmírnění rizik dlouhodobého kompromitování klíče. Jeho specifikace napříč více releasy zajišťuje zpětnou kompatibilitu a přizpůsobení se vyvíjejícím se architekturám MBMS, včetně vylepšení pro LTE Broadcast (eMBMS) a 5G Broadcast.

## Klíčové vlastnosti

- Symetrický šifrovací klíč pro zabezpečení provozu na aplikační vrstvě MBMS (např. video, soubory).
- Generován a spravován Broadcast Multicast Service Centre (BM-SC).
- Distribuován k UE v zašifrované formě, přičemž je chráněn pomocí MBMS Service Key (MSK).
- Podporuje periodickou obnovu a aktualizace pro udržení dlouhodobé bezpečnosti vysílacích služeb.
- Umožňuje škálovatelnou ochranu obsahu pro masivní počty současných příjemců.
- Integrální součást hierarchie bezpečnostních klíčů MBMS, spolupracuje s MSK a MUK.

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MSK – Minimum-shift keying](/mobilnisite/slovnik/msk/)
- [MUK – Multicast User Key](/mobilnisite/slovnik/muk/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.246** (Rel-19) — MBMS Security Specification
- **TS 33.888** (Rel-12) — Security Study for Group Communication in LTE

---

📖 **Anglický originál a plná specifikace:** [MTK na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtk/)
