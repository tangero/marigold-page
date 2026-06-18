---
slug: "kms"
url: "/mobilnisite/slovnik/kms/"
type: "slovnik"
title: "KMS – Key Management Service"
date: 2026-01-01
abbr: "KMS"
fullName: "Key Management Service"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/kms/"
summary: "Funkční entita nebo služba v architekturách 3GPP odpovědná za generování, distribuci, uložení a správu životního cyklu kryptografických klíčů. Je klíčová pro zabezpečení komunikací, zejména u služeb z"
---

KMS je funkční entita v architekturách 3GPP odpovědná za generování, distribuci, uložení a správu životního cyklu kryptografických klíčů pro zabezpečení komunikací.

## Popis

Služba správy klíčů (Key Management Service, KMS) v 3GPP je kritická bezpečnostní funkce, která poskytuje komplexní správu kryptografických klíčů pro různé síťové služby a aplikace. Není to jediná monolitická entita, ale konceptuální služba, kterou lze implementovat napříč různými síťovými architekturami, včetně IP multimediální podsystému (IP Multimedia Subsystem, IMS), služeb pro kritickou komunikaci (Mission Critical Services, [MCS](/mobilnisite/slovnik/mcs/)) a systémů 5G. KMS je odpovědná za celý životní cyklus klíče: generování (nebo získání z kořenového klíče), zabezpečenou distribuci, aktivaci, deaktivaci, obnovu (rotaci), odvolání a smazání klíčů. Zajišťuje, že klíče jsou dostupné autorizovaným entitám – jako je uživatelské zařízení (UE), aplikační servery a síťové funkce – kdykoli je to potřeba, a jsou chráněny před neoprávněným přístupem.

Z architektonického hlediska může být KMS integrována do konkrétních síťových funkcí nebo nasazena jako samostatná centralizovaná služba. Ve službách založených na IMS, jako je Voice over LTE (VoLTE) nebo Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)), KMS často komunikuje s infrastrukturou pro autentizaci, autorizaci a účtování (Authentication, Authorization, and Accounting, [AAA](/mobilnisite/slovnik/aaa/)), serverem [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) a aplikačními servery. Například v MCPTT KMS generuje a distribuuje služebně specifické klíče, jako je Kmcptt, z nichž jsou odvozeny další klíče (např. [KFC-ID](/mobilnisite/slovnik/kfc-id/), klíče pro šifrování médií). Pro zabezpečené doručování klíčů přes IP sítě používá standardizované protokoly, jako je Key Management Protocol (KMP) definovaný v 3GPP TS 33.179 a 33.180. KMS může také spolupracovat s infrastrukturou veřejných klíčů (Public Key Infrastructure, [PKI](/mobilnisite/slovnik/pki/)) pro správu certifikátů nebo s hardwarovými bezpečnostními moduly (Hardware Security Modules, HSM) pro zabezpečené generování a ukládání klíčů.

Při provozu KMS spolupracuje s autentizačními procedurami. Po úspěšné autentizaci uživatele nebo zařízení je KMS vyvolána, aby poskytla potřebné klíče na aplikační úrovni. To může být spuštěno na žádost aplikačního serveru. KMS autentizuje žadatele, ověří autorizační politiky a poté zabezpečeně doručí klíčový materiál, často zašifrovaný pomocí předem sdíleného klíče nebo klíče vytvořeného během autentizace přístupu k síti. V kontextech 5G a síťového řezání může KMS podporovat správu klíčů specifickou pro síťový řez (slice), čímž zajišťuje izolaci mezi řezy správou samostatných klíčových hierarchií. Také zvládá správu skupinových klíčů pro služby multicast/broadcast nebo skupinovou komunikaci, efektivně distribuuje a aktualizuje klíče pro více členů.

Její role je zásadní pro umožnění pokročilých bezpečnostních funkcí, jako je end-to-end šifrování, dopředná bezpečnost (forward secrecy) a zabezpečené zavádění služeb (onboarding). Centralizací správy klíčů KMS snižuje složitost a bezpečnostní rizika spojená s ad-hoc správou klíčů jednotlivými aplikacemi. Poskytuje záznamy auditu, politiky používání klíčů a soulad s kryptografickými standardy. V scénářích kritické komunikace KMS zajišťuje, že nouzová komunikace zůstane zabezpečená, i když jsou části sítě kompromitovány, protože klíče lze rychle odvolat a znovu vydat. KMS je tedy páteří škálovatelné, spravovatelné a robustní kryptografické infrastruktury v moderních sítích 3GPP.

## K čemu slouží

KMS byla zavedena, aby vyřešila rostoucí složitost a bezpečnostní výzvy správy klíčů v rozvíjejících se sítích 3GPP. Jak se služby posouvaly od základního hlasu a [SMS](/mobilnisite/slovnik/sms/) k bohatým IP multimediálním službám (IMS) a aplikacím pro kritickou komunikaci, každá služba vyžadovala vlastní sadu kryptografických klíčů pro důvěrnost, integritu a autentizaci. Samostatná správa těchto klíčů pro každou službu vedla k duplicitě, nekonzistentním bezpečnostním politikám a zvýšené zranitelnosti. KMS byla vytvořena, aby poskytla jednotný, standardizovaný přístup ke správě životního cyklu klíčů napříč různorodými službami.

Historicky dřívější mobilní sítě integrovaly správu klíčů do základních síťových funkcí, jako je [HSS](/mobilnisite/slovnik/hss/)/AuC, které primárně zpracovávaly klíče pro přístupovou autentizaci (např. CK, IK). Tyto však nebyly navrženy pro dynamickou distribuci klíčů na aplikační vrstvu, kterou vyžadují služby jako zabezpečený skupinový chat, push-to-talk nebo šifrované video streamování. Mezi omezení patřil nedostatek škálovatelnosti, absence standardizovaného protokolu pro doručování klíčů aplikačním serverům a slabá podpora správy skupinových klíčů. KMS, formalizovaná od Release 8, tyto mezery vyřešila oddělením správy klíčů od konkrétních přístupových technologií a jejím zpřístupněním jako služby pro jakoukoli autorizovanou síťovou funkci nebo aplikaci.

Její vývoj byl dále motivován potřebou regulatorní shody a interoperability v komunikacích pro veřejnou bezpečnost (Mission Critical Services). Orgány vyžadovaly zaručenou bezpečnost s kontrolou nad kryptografickým materiálem, což mohla poskytnout dedikovaná KMS. V 5G, s příchodem síťového řezání, se účel KMS rozšířil o umožnění izolované bezpečnosti pro síťové řezy, kde každý síťový řez může mít vlastní politiky správy klíčů a klíčové prostory. Centralizací a standardizací správy klíčů KMS snižuje provozní náklady, zlepšuje bezpečnostní postavení prostřednictvím konzistentních politik a umožňuje rychlé nasazení nových zabezpečených služeb, což s fragmentovanými přístupy minulosti nebylo možné.

## Klíčové vlastnosti

- Centralizovaná správa životního cyklu (generování, distribuce, obnova, odvolání) kryptografických klíčů
- Podporuje správu individuálních i skupinových klíčů pro multicast/broadcast služby
- Integruje se s autentizačními systémy (např. 5G AKA, EAP) pro vázání klíčů na identitu uživatele/zařízení
- Používá standardizované protokoly pro správu klíčů (Key Management Protocols, KMP) pro zabezpečené doručování klíčů přes IP sítě
- Umožňuje služebně specifické klíčové hierarchie (např. pro MCPTT, MIoT) a end-to-end šifrování
- Poskytuje vynucování politik, auditování a zabezpečené ukládání, často s rozhraním k hardwarovým bezpečnostním modulům (Hardware Security Modules, HSM)

## Definující specifikace

- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 24.883** (Rel-16) — MCPTT Interworking with LMR Systems
- **TS 29.379** (Rel-19) — MCPTT call control interworking with LMR systems
- **TS 29.828** (Rel-12) — IMS Media Plane Security H.248 Profiles Study
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.328** (Rel-19) — IMS Media Plane Security Specification
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [KMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/kms/)
