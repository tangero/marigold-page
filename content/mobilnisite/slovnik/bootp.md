---
slug: "bootp"
url: "/mobilnisite/slovnik/bootp/"
type: "slovnik"
title: "BOOTP – Bootstrap Protocol"
date: 2026-01-01
abbr: "BOOTP"
fullName: "Bootstrap Protocol"
category: "Management"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/bootp/"
summary: "BOOTP je síťový managementový protokol standardizovaný 3GPP pro inicializaci síťových prvků a poskytování konfiguračních dat. Umožňuje automatickou konfiguraci zařízení poskytováním IP adres, softwaro"
---

BOOTP je síťový managementový protokol standardizovaný 3GPP, který automatizuje startovní konfiguraci síťových prvků poskytováním IP adres, softwarových obrazů a provozních parametrů.

## Popis

Bootstrap Protocol (BOOTP) slouží v sítích 3GPP jako základní managementový protokol pro inicializaci síťových prvků během startu systému a pro provisioningové operace. BOOTP funguje jako klient-server protokol, kde síťové prvky (klienti) žádají o konfigurační informace ze serverů BOOTP během své inicializační fáze. Protokol používá jako transportní mechanismus UDP, typicky na známých portech 67 (server) a 68 (klient), a využívá broadcastové zprávy pro objevování dostupných serverů, když klient nemá předchozí konfiguraci sítě.

Z architektonického hlediska zahrnuje BOOTP několik klíčových komponent: klienta BOOTP integrovaného v síťových prvcích, jeden nebo více serverů BOOTP, které udržují databáze konfigurací, a volitelně relay agenty, kteří přeposílají zprávy BOOTP přes hranice sítí. Protokolová výměna začíná, když klient vyšle broadcastem paket BOOTP request obsahující jeho hardwarovou adresu ([MAC](/mobilnisite/slovnik/mac/) adresu) a transakční identifikátor. Servery BOOTP přijímající tuto žádost konzultují své konfigurační databáze, aby přiřadily hardwarové adrese klienta předdefinované konfigurační parametry, a poté odpoví paketem BOOTP reply obsahujícím přiřazenou konfiguraci.

Konfigurační data poskytovaná prostřednictvím BOOTP typicky zahrnují IP adresu klienta, masku podsítě, výchozí bránu, název bootovacího souboru (pro získání softwarového obrazu přes TFTP) a různé síťově specifické parametry. V sítích 3GPP je BOOTP zvláště cenný pro provisioning síťových prvků, jako jsou základnové stanice, uzly core sítě a managementové systémy, které vyžadují konzistentní, automatizovanou konfiguraci napříč rozsáhlými nasazeními. Jednoduchost a spolehlivost protokolu jej činí vhodným pro scénáře počátečního zprovoznění sítě, kdy složitější managementové protokoly nemusí být ještě dostupné.

Role BOOTP přesahuje základní přiřazování IP adres a zahrnuje správu softwarových verzí a vynucování konzistence konfigurace. Síťoví operátoři mohou udržovat centralizované konfigurační databáze na serverech BOOTP, což zajišťuje, že všechny síťové prvky obdrží odpovídající konfiguraci na základě svých hardwarových identifikátorů, umístění nebo funkční role. Tento centralizovaný přístup usnadňuje škálovatelnost sítě, snižuje chyby při ruční konfiguraci a umožňuje rychlé nasazení nových síťových prvků bez nutnosti přítomnosti technického personálu na místě pro počáteční nastavení.

Fungování protokolu zahrnuje mechanismy pro práci s více servery, prevenci duplicitních adres a perzistenci konfigurace. Servery BOOTP mohou být nakonfigurovány s překrývajícími se rozsahy nebo schopnostmi převzetí služeb při selhání (failover), aby byla zajištěna vysoká dostupnost konfigurační služby. Zatímco samotný BOOTP neobsahuje bezpečnostní funkce, specifikace 3GPP často doporučují jeho nasazení v zabezpečených síťových segmentech nebo jeho kombinaci s dodatečnými bezpečnostními opatřeními, aby se zabránilo neautorizovaným změnám konfigurace nebo vydávání se za síťový prvek.

## K čemu slouží

BOOTP byl vyvinut, aby řešil provozní výzvy správy rozsáhlých telekomunikačních sítí se stovkami nebo tisíci síťových prvků vyžadujících konzistentní, automatizovanou konfiguraci. Před protokoly jako BOOTP čelili síťoví operátoři značnému manuálnímu úsilí při konfiguraci každého síťového prvku individuálně, což vedlo k nekonzistencím v konfiguraci, zpožděním v nasazení a zvýšeným provozním nákladům. Vytvoření protokolu bylo motivováno potřebou škálovatelných řešení pro správu sítí, která by mohla podporovat rychlou expanzi sítí 3GPP a rostoucí složitost konfigurací síťových prvků.

Historicky se konfigurace síťových prvků spoléhala na manuální metody, sériová konzolová připojení nebo proprietární managementová řešení, která se neškálovala efektivně. Jak se sítě 3GPP vyvíjely z malých pilotních nasazení na celostátní komerční sítě, omezení těchto přístupů se stala zřejmými. BOOTP poskytl standardizované, výrobně neutrální řešení pro počáteční konfiguraci síťových prvků, které mohlo být implementováno napříč různorodým vybavením od více výrobců. Tato standardizace byla zvláště důležitá pro zajištění interoperability v síťových prostředích s více dodavateli.

Protokol řeší několik klíčových problémů: odstraňuje nutnost předkonfigurace síťových prvků před nasazením, snižuje čas potřebný k uvedení nových síťových prvků do provozu, zajišťuje konzistenci konfigurace napříč podobnými síťovými prvky a umožňuje vzdálenou správu síťových prvků i když jim chybí počáteční síťová konfigurace. Automatizací procesu počáteční konfigurace umožňuje BOOTP síťovým operátorům nasazovat, nahrazovat nebo upgradovat síťové prvky s minimálním manuálním zásahem, což významně zlepšuje provozní efektivitu a snižuje potenciál lidské chyby v kritických úlohách konfigurace sítě.

## Klíčové vlastnosti

- Automatické přiřazení IP adresy během inicializace síťového prvku
- Centralizovaná správa konfigurace prostřednictvím serverů BOOTP
- Podpora pro provisioning softwarových obrazů prostřednictvím specifikace bootovacího souboru
- Identifikace klienta a mapování konfigurace založené na hardwarové adrese
- Objevování serverů založené na broadcastu pro klienty bez síťové konfigurace
- Rozšiřitelnost konfiguračních parametrů prostřednictvím výrobně specifických voleb

## Související pojmy

- [DHCP – Dynamic Host Configuration Protocol](/mobilnisite/slovnik/dhcp/)

## Definující specifikace

- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security

---

📖 **Anglický originál a plná specifikace:** [BOOTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bootp/)
