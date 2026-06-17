---
slug: "bia"
url: "/mobilnisite/slovnik/bia/"
type: "slovnik"
title: "BIA – BootstrappingInfo-Answer message"
date: 2025-01-01
abbr: "BIA"
fullName: "BootstrappingInfo-Answer message"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bia/"
summary: "BootstrappingInfo-Answer (BIA) je zpráva protokolu Diameter používaná v architektuře Generic Authentication Architecture (GAA) dle 3GPP. Je odesílána funkcí Bootstrapping Server Function (BSF) funkci"
---

BIA je zpráva protokolu Diameter odesílaná funkcí Bootstrapping Server Function (BSF) funkci Network Application Function (NAF) za účelem bezpečného doručení bootstrapovacích informací pro autentizaci na aplikační vrstvě.

## Popis

BootstrappingInfo-Answer (BIA) je odpověď založená na protokolu Diameter, definovaná v 3GPP TS 29.109, která funguje v rámci architektury Generic Authentication Architecture ([GAA](/mobilnisite/slovnik/gaa/)). Je klíčovou součástí rozhraní Zh, které spojuje funkci Bootstrapping Server Function ([BSF](/mobilnisite/slovnik/bsf/)) a funkci Network Application Function ([NAF](/mobilnisite/slovnik/naf/)). Zprávu BIA generuje BSF jako odpověď na zprávu BootstrappingInfo-Request ([BIR](/mobilnisite/slovnik/bir/)) od NAF. Jejím hlavním účelem je bezpečně přenést bootstrapovací informace, včetně identifikátoru bootstrapovací transakce ([B-TID](/mobilnisite/slovnik/b-tid/)) a přidruženého klíčového materiálu, k NAF. To umožňuje NAF autentizovat uživatelské zařízení (UE) a odvodit relakční klíče pro zabezpečení komunikace na aplikační vrstvě, například u služeb Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) nebo zabezpečení uživatelské roviny (User Plane Security).

Z architektonického hlediska je zpráva BIA součástí Diameter aplikace pro GAA a využívá páry atribut-hodnota ([AVP](/mobilnisite/slovnik/avp/)) k zapouzdření kritických bezpečnostních parametrů. Mezi klíčové AVP patří B-TID, který jednoznačně identifikuje bootstrapovací relaci, a AVP Key-Lifetime, které určuje platnost dodaného klíčového materiálu. Zpráva také nese AVP BootstrappingInfo, obsahující vlastní bootstrapovací odpověď, a AVP s výsledkovými kódy (result-code) pro indikaci úspěchu nebo selhání žádosti. BSF před vygenerováním BIA ověřuje žádost NAF vůči svému uloženému bootstrapovacímu kontextu, čímž zajišťuje, že citlivý klíčový materiál obdrží pouze autorizované NAF.

Během provozu, když se UE pokusí přistoupit ke službě vyžadující autentizaci založenou na GAA, odešle NAF BIR k BSF. BSF tuto žádost zpracuje ověřením poskytnutého B-TID a kontrolou, zda je NAF autorizována pro požadovanou službu. Po úspěšném ověření BSF sestaví zprávu BIA a naplní ji potřebnými bootstrapovacími informacemi a kryptografickými klíči odvozenými z počátečního procedury [AKA](/mobilnisite/slovnik/aka/) (Authentication and Key Agreement) mezi UE a BSF. BIA je poté přenesena přes zabezpečené rozhraní Zh k NAF, která použije obsažená data k autentizaci UE a navázání zabezpečené aplikační relace. Tento proces eliminuje potřebu, aby UE uchovávalo více přihlašovacích údajů pro jednotlivé aplikace, a využívá stávající autentizaci předplatného 3GPP.

Zpráva BIA hraje zásadní roli při umožnění škálovatelného a bezpečného přístupu ke službám napříč různorodými aplikacemi 3GPP i mimo ně. Centralizací bootstrapování na BSF a distribucí klíčového materiálu prostřednictvím standardizovaných zpráv, jako je BIA, zajišťuje GAA konzistentní bezpečnostní postupy a snižuje režii správy přihlašovacích údajů. Návrh zprávy podporuje rozšiřitelnost prostřednictvím volitelných AVP, což umožňuje budoucí vylepšení bez narušení stávajících implementací. Její integrace s protokolem Diameter zajišťuje spolehlivé, spojově orientované doručování a interoperabilitu s dalšími prvky jádra sítě 3GPP.

## K čemu slouží

Zpráva BootstrappingInfo-Answer (BIA) byla zavedena v 3GPP Release 8 jako součást architektury Generic Authentication Architecture (GAA) jako odpověď na rostoucí potřebu bezpečných a škálovatelných autentizačních mechanismů pro síťové aplikace mimo tradiční mobilní služby. Před GAA aplikace jako MBMS nebo IP Multimedia Subsystem (IMS) často vyžadovaly samostatné autentizační frameworky, což vedlo k fragmentovaným bezpečnostním modelům, zvýšené složitosti správy přihlašovacích údajů a špatné uživatelské zkušenosti kvůli opakovaným přihlášením. GAA, s BIA jako klíčovým protokolovým prvkem, využívá stávající infrastrukturu 3GPP AKA k bootstrapování zabezpečení pro širokou škálu služeb, čímž odstraňuje potřebu aplikací specifických uživatelských přihlašovacích údajů a zjednodušuje autentizační prostředí.

Vznik BIA byl motivován posunem průmyslu ke konvergovaným službám, kde jediná autentizační událost na síťové vrstvě může umožnit bezpečný přístup k více aplikacím. Tento přístup snižuje signalizační režii, zvyšuje bezpečnost opětovným využíváním prověřených protokolů 3GPP AKA a snižuje provozní náklady centralizací správy klíčů na BSF. Zpráva BIA konkrétně řeší problém bezpečné distribuce bootstrapovacích informací z BSF k autorizovaným NAF, což zajišťuje, že citlivý klíčový materiál je přenášen standardizovaným a chráněným způsobem přes rozhraní Zh. To umožňuje aplikacím nezávisle autentizovat uživatele bez přímého přístupu k Home Subscriber Server (HSS) nebo nutnosti zadávání hesel uživatelem.

Historicky se řešení před GAA spoléhala na ad-hoc autentizační metody nebo duplikované procedury AKA, které byly neefektivní a nejisté. BIA jako součást GAA poskytla standardizovaný, do budoucna připravený mechanismus, který podporoval nově vznikající služby jako mobilní TV, zabezpečený podnikový přístup a komunikace typu stroj-stroj (M2M). Její návrh zajišťuje zpětnou kompatibilitu a rozšiřitelnost, což jí umožňuje vyvíjet se prostřednictvím následných vydání 3GPP, aby vyhověla novým případům užití a zvýšeným bezpečnostním požadavkům, jako jsou ty pro IoT a síťové segmenty (network slicing).

## Klíčové vlastnosti

- Zpráva založená na protokolu Diameter pro bezpečné doručení bootstrapovacích informací
- Nese identifikátor bootstrapovací transakce (B-TID) a klíčový materiál pro zabezpečení na aplikační vrstvě
- Umožňuje NAF autentizovat UE a odvodit relakční klíče bez samostatných přihlašovacích údajů
- Podporuje rozšiřitelné páry atribut-hodnota (AVP) pro budoucí vylepšení
- Integruje se s 3GPP AKA za účelem opětovného využití autentizace mobilního předplatného
- Poskytuje výsledkové kódy (result codes) pro indikaci úspěchu nebo selhání bootstrapovacích žádostí

## Definující specifikace

- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)

---

📖 **Anglický originál a plná specifikace:** [BIA na 3GPP Explorer](https://3gpp-explorer.com/glossary/bia/)
