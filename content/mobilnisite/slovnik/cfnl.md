---
slug: "cfnl"
url: "/mobilnisite/slovnik/cfnl/"
type: "slovnik"
title: "CFNL – Communication session Forwarding on No Logged-in"
date: 2026-01-01
abbr: "CFNL"
fullName: "Communication session Forwarding on No Logged-in"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cfnl/"
summary: "CFNL je doplňková služba, která přesměruje příchozí komunikační relace, když není zařízení uživatele přihlášeno do sítě. Zajišťuje kontinuitu relace přesměrováním hovorů na alternativní cíle, čímž zab"
---

CFNL je doplňková služba, která přesměruje příchozí komunikační relace na alternativní cíl, když není zařízení uživatele přihlášeno do sítě, čímž zajišťuje kontinuitu a zabraňuje zmeškání hovorů.

## Popis

Communication session Forwarding on No Logged-in (CFNL) je standardizovaná doplňková služba 3GPP, která funguje v rámci architektury IP Multimedia Subsystem (IMS). Když není uživatelské zařízení (UE) registrováno v síti – ať už proto, že je vypnuté, mimo dosah sítě, nebo neprovedlo počáteční registraci – síť nemůže navázat přímou relaci k tomuto UE. CFNL poskytuje mechanismus pro zachycení těchto příchozích požadavků na relaci a jejich přesměrování na předem nakonfigurovaný alternativní cíl, jako je jiné telefonní číslo, hlasová schránka nebo aplikační server. Službu vyvolá Serving-Call Session Control Function (S-CSCF), když zjistí, že cílový uživatel není aktuálně přihlášen do sítě, na základě informací o stavu registrace uložených v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)).

Technická implementace CFNL zahrnuje koordinaci několika síťových prvků. Když dorazí na S-CSCF příchozí požadavek Session Initiation Protocol (SIP) INVITE pro uživatele, který není registrován, S-CSCF zkontroluje profil služeb uživatele získaný z HSS. Pokud je CFNL pro tohoto uživatele aktivní, S-CSCF použije příslušnou přesměrovací logiku na základě konfigurace uživatele. Cíl přesměrování je specifikován v servisních datech uživatele, která mohou zahrnovat podmínky, jako jsou časová omezení nebo různé cíle přesměrování pro různé volající strany. S-CSCF následně upraví SIP požadavek nahrazením původního Request-URI adresou pro přesměrování a pokračuje v navazování relace směrem k novému cíli.

CFNL funguje ve spolupráci s dalšími přesměrovacími službami, jako je Communication Forwarding Unconditional ([CFU](/mobilnisite/slovnik/cfu/)), Communication Forwarding on Busy User ([CFB](/mobilnisite/slovnik/cfb/)) a Communication Forwarding on Not Reachable (CFNRc), a poskytuje tak komplexní možnosti správy relací. Na rozdíl od CFNRc, která řeší případy, kdy je uživatel registrován, ale nedostupný (např. kvůli rádiovým podmínkám), se CFNL konkrétně zabývá scénářem, kdy žádná registrace vůbec neexistuje. Služba podporuje jak hlasové, tak multimediální relace v rámci IMS, což ji činí použitelnou pro VoLTE, VoNR a další komunikační služby založené na IMS. Konfigurace a aktivace CFNL může být provedena přes rozhraní Ut pomocí protokolu XCAP nebo prostřednictvím procedur iniciovaných sítí, což uživatelům poskytuje flexibilitu při správě jejich přesměrovacích preferencí.

Z pohledu síťové architektury je CFNL silně závislá na integraci mezi S-CSCF a HSS. HSS ukládá servisní data CFNL jako součást IMS profilu služeb uživatele, včetně adresy pro přesměrování a případných platných podmínek. Když S-CSCF obdrží trigger initial filter criteria (iFC) pro neregistrovaného uživatele, provede příslušný Service Point Trigger (SPT), který vyvolá logiku aplikačního serveru CFNL. Aplikační server, který může být integrován v rámci S-CSCF nebo implementován jako samostatný [AS](/mobilnisite/slovnik/as/), následně zpracuje rozhodnutí o přesměrování. Tato architektura zajišťuje, že CFNL funguje konzistentně napříč různými nasazeními sítí a implementacemi dodavatelů při zachování shody se specifikacemi 3GPP.

## K čemu slouží

CFNL bylo zavedeno, aby řešilo základní omezení v mobilních komunikačních systémech: neschopnost kontaktovat uživatele, když jejich zařízení není aktivně registrováno v síti. Před standardizací CFNL sítě obvykle odmítaly příchozí relace pro neregistrované uživatele s chybovými odpověďmi jako „480 Temporarily Unavailable“ nebo „404 Not Found“, což vedlo k zameškané komunikaci a špatné uživatelské zkušenosti. To bylo obzvláště problematické, protože uživatelé stále více spoléhali na mobilní zařízení jako na svůj primární komunikační prostředek a očekávali spolehlivé připojení, i když byla jejich zařízení dočasně offline.

Služba řeší problém ztráty komunikace během období, kdy uživatelské zařízení (UE) nemůže udržet síťovou registraci z různých důvodů, včetně úspory energie, dlouhodobého pobytu mimo dosah sítě nebo manuálního vypnutí zařízení. Poskytnutím standardizovaného mechanismu pro přesměrování relací na alternativní cíle CFNL zajišťuje, že důležitá komunikace není ztracena, ale je přesměrována podle preferencí uživatele. Tato schopnost je zvláště cenná pro firemní uživatele, kteří si nemohou dovolit zmeškat důležité hovory, a pro scénáře nouzové komunikace, kde je spolehlivý kontakt zásadní.

Vznik CFNL byl motivován evolucí směrem k plně IP sítím a architektuře IMS ve 3GPP Release 7. Jak sítě přecházely z okruhově přepínané domény na paketově přepínanou, vznikla potřeba replikovat a vylepšit tradiční doplňkové služby v novém prostředí založeném na IP. CFNL představuje ekvivalent služby „Forwarding on Mobile Subscriber Not Reachable“ z okruhově přepínané domény v prostředí IMS, ale s rozšířenými schopnostmi pro multimediální relace. Služba reaguje na rostoucí očekávání „vždy dostupné“ komunikace v moderních mobilních sítích a zároveň poskytuje uživatelům kontrolu nad tím, jak je s jejich komunikací nakládáno během offline období.

## Klíčové vlastnosti

- Přesměruje příchozí relace, když není uživatelské zařízení registrováno v síti
- Podporuje jak hlasové, tak multimediální komunikační relace v rámci IMS
- Konfigurovatelné cíle přesměrování včetně čísel, hlasové schránky nebo aplikačních serverů
- Integruje se s HSS pro data o účastnících a s S-CSCF pro řízení relace
- Funguje na základě initial filter criteria a service point triggers v IMS
- Lze konfigurovat a aktivovat přes rozhraní Ut pomocí protokolu XCAP

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [CFU – Communication Forwarding Unconditional](/mobilnisite/slovnik/cfu/)
- [CFNR – Communication Forwarding No Reply](/mobilnisite/slovnik/cfnr/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.516** (Rel-8) — MCID Protocol Specification for NGN
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 24.606** (Rel-19) — MWI Service Protocol Description
- **TS 24.615** (Rel-19) — Communication Waiting (CW) Service Protocol
- **TS 24.616** (Rel-19) — Malicious Call Identification (MCID) Protocol
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [CFNL na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfnl/)
