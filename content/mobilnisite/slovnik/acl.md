---
slug: "acl"
url: "/mobilnisite/slovnik/acl/"
type: "slovnik"
title: "ACL – Asynchronous Connection-Oriented Link"
date: 2025-01-01
abbr: "ACL"
fullName: "Asynchronous Connection-Oriented Link"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/acl/"
summary: "Typ spojení v Bluetooth poskytující spolehlivý, sekvenovaný přenos dat mezi zařízeními s využitím časových slotů. Podporuje spojení bod-bod s mechanismy opakovaného vysílání pro opravu chyb, což je kl"
---

ACL je typ spojení v Bluetooth pro spolehlivý, sekvenovaný přenos dat bod-bod využívající časové sloty a mechanismy opakovaného vysílání, fungující vedle spojení SCO.

## Popis

Asynchronní spojově orientované spojení (ACL) je základní transportní mechanismus Bluetooth, který zajišťuje spolehlivou, spojově orientovanou datovou komunikaci mezi hlavním zařízením a jedním či více podřízenými zařízeními v pikosíti. Na rozdíl od synchronních spojově orientovaných (SCO) spojení určených pro izochronní hlasový provoz, spojení ACL zpracovávají asynchronní přenos dat s vestavěnými schopnostmi detekce chyb a opakovaného vysílání. ACL funguje na architektuře hlavní-podřízený, kde hlavní zařízení řídí časování a dotazování podřízených zařízení a přiděluje časové sloty pro obousměrný nebo jednosměrný přenos dat.

Spojení ACL využívají schéma časového duplexu (TDD), kde se hlavní a podřízené zařízení střídají ve vysílání v po sobě jdoucích časových slotech. Hlavní zařízení zahajuje komunikaci v sudých slotech a adresované podřízené zařízení odpovídá v následujícím lichém slotu. Tento dotazovací mechanismus umožňuje hlavnímu zařízení udržovat spojení až se sedmi aktivními podřízenými zařízeními v pikosíti. Pakety ACL podporují různé velikosti užitečného zatížení a datové rychlosti, přičemž základní rychlost nabízí 723,2 kbps asymetrického nebo 433,9 kbps symetrického přenosu dat. Režimy zvýšené datové rychlosti (EDR) zavedené v pozdějších verzích Bluetooth výrazně zvyšují propustnost.

Řízení chyb ve spojeních ACL využívá mechanismy automatického opakovaného dotazu ([ARQ](/mobilnisite/slovnik/arq/)) s cyklickým redundantním součtem ([CRC](/mobilnisite/slovnik/crc/)) a dopřednou korekcí chyb ([FEC](/mobilnisite/slovnik/fec/)) pro určité typy paketů. Hlavní zařízení používá protokol ARQ typu stop-and-wait, kde musí být každý vyslaný paket potvrzen před odesláním dalšího. Nepotvrzené pakety jsou znovu vysílány, dokud nedojde k úspěšnému doručení nebo do vypršení časového limitu. ACL podporuje více typů paketů s různou úrovní ochrany proti chybám, což umožňuje kompromisy mezi spolehlivostí a propustností podle požadavků aplikace.

Spojení ACL koexistují se spojeními SCO v sítích Bluetooth prostřednictvím časového multiplexování. Hlavní zařízení plánuje oba typy spojení v rámci stejné pikosítě, přičemž spojení SCO mají prioritu pro svůj časově kritický hlasový provoz. Provoz ACL vyplňuje zbývající časové sloty a poskytuje tak efektivní využití šířky pásma. Tato architektura s dvojím spojením umožňuje zařízením Bluetooth současně podporovat hlasové hovory a aplikace pro přenos dat. ACL také tvoří základ pro pokročilé profily a služby Bluetooth vyžadující spolehlivý přenos dat.

## K čemu slouží

ACL bylo vytvořeno za účelem poskytnutí spolehlivé datové komunikace v sítích Bluetooth, aby bylo možné řešit potřebu bezchybného přenosu aplikačních dat vedle hlasového provozu. Před standardizací Bluetooth se bezdrátový přenos dat často spoléhal na proprietární protokoly s nekonzistentními mechanismy spolehlivosti. ACL zavedlo standardizovaný přístup k asynchronnímu přenosu dat se zaručeným doručením, což umožnilo interoperabilní datové aplikace napříč zařízeními různých výrobců.

Tato technologie řeší problém udržení integrity dat na náchylných bezdrátových kanálech při efektivním sdílení šířky pásma se synchronními hlasovými spojeními. Předchozí řešení bezdrátového přenosu dat buď postrádala správnou opravu chyb, nebo používala neefektivní schémata opakovaného vysílání, která degradovala celkový výkon sítě. Kombinace [ARQ](/mobilnisite/slovnik/arq/), [FEC](/mobilnisite/slovnik/fec/) a flexibilních typů paketů v ACL poskytuje přizpůsobitelnou ochranu proti chybám vhodnou pro různé typy dat a podmínky kanálu.

Vytvoření ACL bylo motivováno rostoucí potřebou technologií pro náhradu kabelů, které by spolehlivě zvládly jak hlasové, tak datové aplikace. Tím, že ACL poskytlo spojově orientovaný přenos dat s mechanismy sekvencování a potvrzování, umožnilo Bluetooth podporovat přenos souborů, přístup k síti, synchronizaci a další datově náročné aplikace. To učinilo Bluetooth vhodným pro širší spektrum případů použití nad rámec jednoduchých hlasových sluchátek, což přispělo k jeho rozšířenému přijetí v mobilních zařízeních, počítačích a aplikacích IoT.

## Klíčové vlastnosti

- Spolehlivý přenos dat s opakovaným vysíláním ARQ
- Spojově orientovaná komunikace se sekvencováním
- Podpora asymetrických a symetrických datových rychlostí
- Koexistence se spojeními SCO prostřednictvím časového multiplexování
- Více typů paketů s různou ochranou proti chybám
- Hlavním zařízením řízené dotazování podřízených zařízení

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 24.235** (Rel-12) — I-WLAN Interworking Management Object
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.305** (Rel-19) — Selective Disabling of 3GPP UE Capabilities
- **TS 24.368** (Rel-19) — NAS Configuration Management Object
- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 28.602** (Rel-12) — CN & non-3GPP NRM IRP Information Service
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TR 31.901** (Rel-14) — USIM/ISIM/USAT Feature Review Study
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [ACL na 3GPP Explorer](https://3gpp-explorer.com/glossary/acl/)
