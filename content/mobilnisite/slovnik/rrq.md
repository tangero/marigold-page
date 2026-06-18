---
slug: "rrq"
url: "/mobilnisite/slovnik/rrq/"
type: "slovnik"
title: "RRQ – MIPv4 Registration Request"
date: 2025-01-01
abbr: "RRQ"
fullName: "MIPv4 Registration Request"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rrq/"
summary: "MIPv4 Registration Request (RRQ) je zpráva protokolu odeslaná mobilním uzlem (Mobile Node, MN) svému domácímu agentovi (Home Agent, HA) v Mobile IPv4. Žádá o vytvoření nebo obnovení vazby mezi domácí"
---

RRQ je zpráva protokolu Mobile IPv4 odeslaná mobilním uzlem (Mobile Node) svému domácímu agentovi (Home Agent) s žádostí o vytvoření nebo obnovení vazby (binding), čímž umožňuje tunelování paketů na aktuální umístění uzlu pro podporu mobility.

## Popis

MIPv4 Registration Request (RRQ) je iniciální zpráva v registrační proceduře Mobile IPv4 (MIPv4), odeslaná mobilním uzlem (Mobile Node, [MN](/mobilnisite/slovnik/mn/)) svému domácímu agentovi (Home Agent, [HA](/mobilnisite/slovnik/ha/)). Jejím účelem je informovat HA o aktuálním připojovacím bodu MN k internetu, reprezentovaném přechodnou adresou (Care-of Address, CoA), a požádat, aby HA tuto CoA navázal na stálou domácí adresu (Home Address) MN. Tato vazba je klíčová pro IP mobilitu, neboť nařizuje HA zachytávat pakety určené pro domácí adresu a přesměrovávat je pomocí IP-in-IP enkapsulace na CoA.

Paket RRQ je konstruován dle specifikace MIPv4 ([RFC](/mobilnisite/slovnik/rfc/) 5944). Obsahuje povinná pole, jako je domácí adresa MN, adresa domácího agenta a registrovaná přechodná adresa. Kritickým polem je Identifikace (Identification), 64bitové číslo generované MN, které slouží ke spárování této žádosti s následnou registrační odpovědí (Registration Response, [RRP](/mobilnisite/slovnik/rrp/)) a k ochraně proti opětovnému přehrání (replay attack). RRQ také specifikuje požadovanou životnost (Lifetime) vazby, po jejímž uplynutí vazba zanikne, pokud není obnovena. Často jsou zahrnuta rozšíření, nejdůležitější z nich je Mobile-Home Authentication Extension, které obsahuje digitální podpis (pomocí sdíleného tajemství) k prokázání identity MN a ochraně integrity zprávy.

RRQ může být odesláno přímo HA, pokud má MN ko-lokovanou CoA, nebo může být přeposláno přes cizího agenta (Foreign Agent, [FA](/mobilnisite/slovnik/fa/)) přítomného v navštívené síti. Při použití FA odešle MN RRQ FA, který jej pak přepošle HA. FA může také přidat do zprávy svou vlastní CoA. Po odeslání RRQ spustí MN opakovací časovač; pokud není přijata RRP, žádost znovu odešle. Tento proces nastává vždy, když MN získá novou CoA (např. po přesunu do nové podsítě), nebo když stávající vazba blíží vypršení a potřebuje obnovení.

V kontextu standardů 3GPP je RRQ využíváno jako součást procedur režimu MIPv4 FA definovaných pro spolupráci s ne-3GPP přístupovými sítěmi, jako je [WLAN](/mobilnisite/slovnik/wlan/). UE (vystupující jako MN) by odeslalo RRQ, aby zaregistrovalo svou CoA (poskytnutou WLAN přístupovou sítí) u funkce domácího agenta sídlící v 3GPP Packet Data Network Gateway ([PDN](/mobilnisite/slovnik/pdn/) GW). To umožňuje UE zachovat IP konektivitu přes 3GPP core síť, zatímco je fyzicky připojeno přes WLAN.

## K čemu slouží

MIPv4 Registration Request existuje k zahájení procesu vytváření mobility vazby, což je klíčový mechanismus umožňující zařízení být dosažitelné na konstantní IP adrese při pohybu mezi různými IP podsítěmi. Základní problém, který řeší, je konflikt mezi směrovací architekturou internetu, která předpokládá, že IP adresa označuje pevné síťové umístění, a potřebou mobilních zařízení měnit svůj fyzický připojovací bod. Bez RRQ k signalizaci nového umístění by se mobilní uzel po přesunu stal nedosažitelným.

Vytvoření RRQ a protokolu MIPv4 bylo motivováno snahou o bezproblémovou mobilitu na síťové vrstvě pro IP hostitele. Předchozí řešení byla specifická pro aplikace nebo spoléhala na mechanismy linkové vrstvy, které se neškálovaly napříč heterogenními sítěmi. RRQ poskytuje standardizovaný, bezpečný a efektivní způsob, jak může mobilní uzel proaktivně oznámit svou novou polohu subjektu (domácímu agentovi) zodpovědnému za správu jeho dosažitelnosti. To umožňuje všem korespondenčním uzlům pokračovat v odesílání paketů na stabilní domácí adresu, aniž by si mobility všimly.

3GPP přijalo MIPv4 a zprávu RRQ, aby splnilo specifické požadavky na mobilitu v raných scénářích spolupráce, zejména s [WLAN](/mobilnisite/slovnik/wlan/). Řešilo omezení vlastní mobility 3GPP založené na GTP, která byla optimalizována pro ekosystém 3GPP, ale ne pro externí IP sítě. RRQ poskytlo známou, IETF-standardizovanou metodu, jak se může UE zaregistrovat do 3GPP core sítě z externí přístupové sítě, což operátorům umožnilo nabízet integrované služby. Sloužilo jako most mezi ne-3GPP IP přístupem a 3GPP packet core, než se preferovaným síťovým řešením stala komplexnější Proxy Mobile IPv6 (PMIPv6).

## Klíčové vlastnosti

- Iniciuje proceduru aktualizace vazby mezi mobilním uzlem a jeho domácím agentem
- Nese aktuální přechodnou adresu mobilního uzla a požadovanou životnost vazby
- Obsahuje jedinečné pole Identifikace pro párování zpráv a ochranu proti opětovnému přehrání
- Podporuje autentizační rozšíření pro bezpečné prokázání identity mobilního uzla
- Může být odesláno přímo nebo přes cizího agenta působícího jako přeposílač
- Spouští u domácího agenta vytvoření tunelu pro přesměrování IP paketů

## Související pojmy

- [RRP – MIPv4 Registration Response](/mobilnisite/slovnik/rrp/)

## Definující specifikace

- **TS 24.304** (Rel-19) — MIPv4 FA Mode Mobility Management in EPC
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.279** (Rel-19) — MIPv4 Mobility Protocol over S2a
- **TS 33.822** (Rel-8) — Security Architecture for Inter-Access Mobility

---

📖 **Anglický originál a plná specifikace:** [RRQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/rrq/)
