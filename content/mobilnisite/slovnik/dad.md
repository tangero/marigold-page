---
slug: "dad"
url: "/mobilnisite/slovnik/dad/"
type: "slovnik"
title: "DAD – Destination ADdress"
date: 2025-01-01
abbr: "DAD"
fullName: "Destination ADdress"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dad/"
summary: "DAD je pole v hlavičkách paketů, které v protokolech sítí 3GPP určuje adresu konečného příjemce. Zajišťuje přesné směrování a doručování uživatelských dat a řídicích zpráv přes rozhraní jako Gn a S5/S"
---

DAD je pole v hlavičce paketu, které určuje adresu konečného příjemce a zajišťuje přesné směrování a doručování datových a řídicích zpráv přes rozhraní sítí 3GPP.

## Popis

Cílová adresa (Destination ADdress, DAD) je základní adresovací prvek používaný v různých protokolových datových jednotkách (PDU) 3GPP k identifikaci zamýšleného koncového bodu pro přenášený paket. Funguje jako klíčový parametr směrování v řídicí a uživatelské rovině, zejména v paketové jádrové síti. DAD není jediná, monolitická adresa, ale konceptuální pole, jehož konkrétní formát a obsah závisí na použité protokolové vrstvě a rozhraní. Například v rámci [GPRS](/mobilnisite/slovnik/gprs/) tunelovacího protokolu ([GTP](/mobilnisite/slovnik/gtp/)) používaného na rozhraních Gn (mezi SGSN nebo SGSN a GGSN) a S5/S8 (mezi S-GW a [P-GW](/mobilnisite/slovnik/p-gw/)) je DAD vloženo do GTP hlaviček. V tomto kontextu typicky obsahuje identifikátor koncového bodu tunelu (TEID) a IP adresu (IPv4 nebo IPv6), která jednoznačně identifikuje přijímající GTP entitu (např. GGSN nebo P-GW) pro konkrétní přenos uživatele. Tato kombinace umožňuje síťovým uzlům demultiplexovat příchozí GTP tunely a správně přiřadit pakety k příslušnému kontextu PDP (Packet Data Protocol) nebo EPS přenosu.

Z architektonického hlediska je DAD klíčovou součástí pro vytváření a udržování GTP tunelů, které tvoří páteř pro přenos uživatelských dat v paketově přepínaných systémech 3GPP. Během procedur, jako je aktivace kontextu PDP nebo nastavení EPS přenosu, si síťové uzly vyjednávají a vyměňují si informace o DAD. Vytvářející entita (např. SGSN nebo S-GW) přiřadí lokální TEID a informuje partnerskou entitu o tomto TEID spolu s vlastní IP adresou, což dohromady tvoří DAD pro provoz směrem vzhůru (uplink) z pohledu partnera. Tato obousměrná výměna zajišťuje, že oba konce tunelu mají potřebné adresovací informace pro správné směrování paketů. DAD tedy umožňuje bezstavové směrování milionů současných uživatelských relací tím, že poskytuje jedinečný, na relaci specifický identifikátor cíle v rámci IP transportní vrstvy jádrové sítě.

Mimo GTP se koncept cílové adresy prolíná i dalšími protokoly a rozhraními 3GPP. V rozhraních založených na protokolu Diameter (např. S6a, Gx) by DAD odpovídalo dvojicím atribut-hodnota ([AVP](/mobilnisite/slovnik/avp/)) Destination-Host a Destination-Realm, které směrují signalizační zprávy na správný [HSS](/mobilnisite/slovnik/hss/) (home subscriber server) nebo PCRF (policy and charging rules function). V rádiové přístupové síti obsahují informaci o cíli také zprávy řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) vrstvy 3, ačkoli je často implicitní v rámci signalizačního spojení specifického pro buňku nebo UE. Spolehlivost a jednoznačnost DAD je prvořadá; jakákoliv porucha nebo chybná konfigurace může vést k chybnému směrování paketů, ztrátě relací nebo bezpečnostním zranitelnostem. Její konzistentní aplikace napříč releasy, jak je uvedeno ve specifikacích, podtrhuje její roli jako základního, stabilního adresovacího primitiva, na kterém jsou vybudovány složitější služby a síťové funkce.

## K čemu slouží

Účelem cílové adresy (Destination ADdress, DAD) je poskytnout standardizovanou, jednoznačnou metodu pro identifikaci příjemce paketu v rámci síťových protokolů definovaných 3GPP. Řeší základní problém směrování paketů a multiplexování relací ve škálovatelné, víceklientské jádrové mobilní síti. Před standardizovanými tunelovacími protokoly, jako je [GTP](/mobilnisite/slovnik/gtp/), rané datové služby postrádaly robustní mechanismus pro efektivní oddělení a směrování provozu pro miliony účastníků přes sdílenou IP páteř. DAD jako součást GTP hlavičky bylo vytvořeno, aby umožnilo vytváření logických point-to-point tunelů (přenosů) mezi síťovými uzly, z nichž každý je jednoznačně identifikován pro konkrétní datovou relaci uživatele. Tato abstrakce umožňuje základní IP transportní síti směrovat pakety na základě adres uzlů, zatímco uzly jádrové sítě používají DAD (TEID + IP) k předávání paketů na správný interní kontext přenosu, což umožňuje efektivní podporu trvalého připojení (always-on) a více současných aplikací na uživatele.

Historicky zavedení [GPRS](/mobilnisite/slovnik/gprs/) a přechod k plně IP jádrové síti ve 3GPP Release 97/98 si vyžádaly tunelovací mechanismus, který by mohl oddělit řídicí a uživatelský provoz a spravovat mobilitu transparentně vůči externím paketovým datovým sítím (PDN). Koncept DAD v rámci GTP byl motivován potřebou udržovat stav relace a kontinuitu směrování, když se uživatelé přesouvali mezi obslužnými uzly. Vyřešil omezení použití pouze IP adresy účastníka pro směrování, což je nedostatečné, protože jediné uživatelské zařízení (UE) může mít více IP adres (pro různé PDN) a stejná IP adresa může být v čase znovu použita různými UE. Začleněním dynamicky přiřazeného TEID specifického pro koncový bod tunelu poskytuje DAD jedinečný identifikátor relace, který je nezávislý na IP adrese uživatele, a zajišťuje tak přesné doručení i během předávání mezi uzly a modifikací relací. Tento návrh je zásadní pro plnění požadavků na kvalitu služeb (QoS) a účtování vyžadovaných architekturami 3GPP.

## Klíčové vlastnosti

- Jednoznačně identifikuje přijímací koncový bod protokolové datové jednotky (PDU) v rozhraních 3GPP
- Základní součást hlaviček GPRS tunelovacího protokolu (GTP) pro tunelování uživatelské a řídicí roviny
- Typicky se skládá z identifikátoru koncového bodu tunelu (TEID) a IP adresy (IPv4/IPv6)
- Umožňuje demultiplexování více logických přenosů končících na stejném fyzickém síťovém uzlu
- Umožňuje bezstavové směrování v transportní síti při zachování stavu relace v jádru
- Základní pro procedury správy mobility, jako jsou předávání a modifikace přenosů

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [DAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/dad/)
