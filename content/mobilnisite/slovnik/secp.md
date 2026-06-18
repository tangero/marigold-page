---
slug: "secp"
url: "/mobilnisite/slovnik/secp/"
type: "slovnik"
title: "SECP – Security Protocol"
date: 2025-01-01
abbr: "SECP"
fullName: "Security Protocol"
category: "Security"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/secp/"
summary: "SECP označuje standardizované bezpečnostní protokoly definované ve specifikacích 3GPP pro ochranu managementových rozhraní a komunikací v telekomunikačních sítích. Tyto protokoly poskytují autentizaci"
---

SECP je standardizovaný bezpečnostní protokol 3GPP pro ochranu síťových managementových rozhraní a komunikací tím, že poskytuje autentizaci, integritu a důvěrnost pro transakce a konfigurační data.

## Popis

Bezpečnostní protokol (SECP) v terminologii 3GPP zahrnuje soubor standardizovaných bezpečnostních mechanismů a protokolů definovaných primárně v TS 32.373 a TS 32.376 pro zabezpečení managementových rozhraní a komunikací v telekomunikačních sítích. Tyto protokoly chrání výměnu managementových informací mezi síťovými prvky, mezi síťovými prvky a managementovými systémy a mezi různými managementovými doménami. Implementace SECP poskytují autentizaci komunikujících entit, ochranu integrity managementových zpráv a důvěrnost citlivých konfiguračních a provozních dat.

SECP funguje aplikací kryptografických bezpečnostních mechanismů na výměny managementových protokolů. Když je zahájena managementová operace – jako je aktualizace konfigurace, načítání dat o výkonu nebo hlášení chyb – implementace SECP vytvoří mezi komunikujícími entitami zabezpečený kontext. To typicky zahrnuje vzájemnou autentizaci pomocí certifikátů nebo sdílených tajemství, vyjednání kryptografických algoritmů a klíčů a vytvoření bezpečnostních asociací. Jakmile je spojení zabezpečeno, jsou managementové zprávy chráněny kódy pro autentizaci zpráv ([MAC](/mobilnisite/slovnik/mac/)) pro integritu a volitelně šifrovány pro důvěrnost. Protokoly fungují na různých vrstvách, přičemž některé implementace SECP zabezpečují přímo aplikační vrstvu managementu, zatímco jiné zabezpečují transportní vrstvu přenášející managementový provoz.

Klíčové součásti SECP zahrnují autentizační mechanismy ověřující identitu managementových entit, procedury správy klíčů pro navázání relací, kryptografické algoritmy pro ochranu integrity (jako HMAC-SHA) a šifrování (jako [AES](/mobilnisite/slovnik/aes/)), stavové automaty bezpečnostních protokolů řídící navázání a udržování zabezpečené relace a body vynucování bezpečnostních politik aplikující ochranu na základě citlivosti managementových operací. Protokoly podporují různá managementová rozhraní včetně těch založených na [CORBA](/mobilnisite/slovnik/corba/), [SNMP](/mobilnisite/slovnik/snmp/), [SOAP](/mobilnisite/slovnik/soap/) nebo RESTful [API](/mobilnisite/slovnik/api/). Role SECP v síti je klíčová pro prevenci neoprávněného přístupu ke konfiguraci sítě, ochranu před manipulací s managementovými daty, která by mohla narušit služby, a zajištění důvěrnosti citlivých provozních informací, které by při zachycení mohly být zneužity k útokům.

## K čemu slouží

SECP byl vytvořen k řešení bezpečnostních zranitelností vlastních síťovým managementovým rozhraním, která se stávala stále více exponovanými, jak telekomunikační sítě přecházely na IP-based management a možnosti vzdálené konfigurace. Tradiční managementová rozhraní často spoléhala na protokoly v čistém textu nebo slabou autentizaci, což je činilo náchylnými k odposlechu, neoprávněnému přístupu a útokům manipulace. Jak se sítě stávaly složitějšími a managementové operace více automatizovanými, potenciální dopad kompromitovaných managementových systémů výrazně rostl, což si vyžádalo standardizované bezpečnostní protokoly.

Tato technologie řeší problém nezabezpečené managementové komunikace poskytováním standardizovaných, kryptograficky silných bezpečnostních mechanismů, které mohou být konzistentně implementovány napříč různými síťovými prvky a managementovými systémy. Řeší konkrétní hrozby včetně neoprávněných konfiguračních změn, které by mohly narušit služby, zachycení citlivých dat o výkonu nebo chybách, které by mohly odhalit síťové zranitelnosti, a útoků vydávání se za legitimní managementové systémy. SECP umožňuje zabezpečený vzdálený management, který je nezbytný pro moderní distribuované síťové architektury a cloudové managementové platformy.

Historicky, jak se síťový management vyvíjel z proprietárních, fyzicky zabezpečených rozhraní na standardizovaný, IP-based vzdálený management, objevily se nové vektory útoků. SECP poskytl potřebný bezpečnostní základ pro tento přechod, zejména když sítě začaly přijímat otevřenější managementové standardy jako SNMPv3, NETCONF a RESTCONF. Protokoly také podporují bezpečnostní požadavky vznikajících managementových paradigmat včetně softwarově definovaných sítí ([SDN](/mobilnisite/slovnik/sdn/)), virtualizace síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)) a autonomního síťového managementu, kde dynamická, programovatelná managementová rozhraní vyžadují robustní zabezpečení, aby se zabránilo rozsáhlým automatizovaným útokům.

## Klíčové vlastnosti

- Vzájemná autentizace managementových entit pomocí certifikátů nebo sdílených tajemství
- Ochrana integrity managementových zpráv prostřednictvím kryptografických mechanismů
- Volitelná ochrana důvěrnosti pro citlivá managementová data
- Podpora více frameworků managementových protokolů (CORBA, SNMP, SOAP, REST)
- Procedury správy klíčů pro navazování zabezpečených relací
- Vynucování bezpečnostních politik na základě citlivosti operace

## Definující specifikace

- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set

---

📖 **Anglický originál a plná specifikace:** [SECP na 3GPP Explorer](https://3gpp-explorer.com/glossary/secp/)
