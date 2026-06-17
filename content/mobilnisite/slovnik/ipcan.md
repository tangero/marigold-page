---
slug: "ipcan"
url: "/mobilnisite/slovnik/ipcan/"
type: "slovnik"
title: "IPCAN – IP Connectivity Access Network"
date: 2025-01-01
abbr: "IPCAN"
fullName: "IP Connectivity Access Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ipcan/"
summary: "IP Connectivity Access Network (IPCAN) je konceptuální rámec v 3GPP, který definuje síťové entity a funkce poskytující IP konektivitu mezi uživatelským zařízením (UE) a externí IP sítí. Je klíčový pro"
---

IPCAN je konceptuální rámec 3GPP definující síťové entity a funkce, které poskytují IP konektivitu mezi uživatelským zařízením (User Equipment) a externí IP sítí.

## Popis

IP Connectivity Access Network (IPCAN) je klíčový architektonický koncept ve specifikacích 3GPP, který modeluje soubor síťových funkcí a přenosových prostředků zodpovědných za poskytování IP konektivity uživateli. Nejde o jednu fyzickou síť, ale o logickou abstrakci zahrnující celou cestu od uživatelského zařízení (UE) k bráně rozhraní s externími paketovými datovými sítěmi (PDN), jako je internet nebo IMS. IPCAN zahrnuje rádiovou přístupovou síť (např. [E-UTRAN](/mobilnisite/slovnik/e-utran/), UTRAN, [GERAN](/mobilnisite/slovnik/geran/), NG-RAN), brány jádra sítě (např. [P-GW](/mobilnisite/slovnik/p-gw/) v EPC, [UPF](/mobilnisite/slovnik/upf/) v 5GC) a propojující přenosovou síť. Jeho hlavní rolí je zřídit jeden nebo více [IP-CAN](/mobilnisite/slovnik/ip-can/) bearerů – logických kanálů se specifickými charakteristikami QoS – pro přenos uživatelských IP dat.

Architektonicky je IPCAN ústřední pro rámec Policy and Charging Control (PCC). Funkce PCRF (Policy and Charging Rules Function) používá IP-CAN relaci jako kontext pro správu. IP-CAN relace představuje asociaci mezi UE a konkrétní PDN, identifikovanou názvem přístupového bodu ([APN](/mobilnisite/slovnik/apn/)). V rámci této relace je zřízen jeden nebo více IP-CAN bearerů. PCRF poskytuje pravidla (PCC pravidla) funkci PCEF (Policy and Charging Enforcement Function), která typicky sídlí v P-GW, a ta tato pravidla instaluje, aby řídila IP-CAN bearety. Toto řízení zahrnuje gating (povolování/blokování paketů), kontrolu QoS (nastavení charakteristik beareru jako [QCI](/mobilnisite/slovnik/qci/), [ARP](/mobilnisite/slovnik/arp/), GBR) a řízení účtování (měření provozu a generování záznamů o účtování).

Provoz IPCAN je dynamický. Když se UE připojí k síti a požádá o připojení k PDN, je zřízena IP-CAN relace. PCEF může iniciovat interakci s PCRF, aby získala počáteční PCC pravidla. Během relace mohou události, jako je mobilita UE, požadavky služeb nebo změny iniciované sítí, způsobit, že PCRF odešle aktualizovaná pravidla, což vede k modifikaci, zřízení nebo ukončení IP-CAN bearerů. To umožňuje přidělování síťových prostředků s ohledem na službu. Například hovor VoLTE (Voice over LTE) spustí zřízení vyhrazeného beareru se zaručenou přenosovou rychlostí (GBR), zatímco synchronizace e-mailů na pozadí využívá výchozí non-GBR bearer. Koncept IPCAN tedy odděluje logiku služeb (řešenou PCRF/AF) od správy konektivity, což umožňuje flexibilní poskytování služeb.

## K čemu slouží

IPCAN byl zaveden, aby poskytl standardizovaný, na technologii nezávislý model pro správu IP konektivity v rámci architektury all-IP jádra sítě 3GPP, která začala s Evolved Packet Core (EPC) ve verzi 8. Před EPC sítě 3GPP (GPRS, UMTS) spravovaly paketové datové kontexty, ale přístup byl těsněji svázán s konkrétními přístupovými technologiemi a postrádal jednotný rámec pro řízení pravidel. Přechod na all-IP síť pro všechny služby, včetně hlasu (prostřednictvím IMS), si vyžádal robustnější, flexibilnější a na pravidlech založenou metodu pro zřizování a řízení IP datových cest.

Vytvoření konceptu IPCAN vyřešilo několik klíčových problémů. Za prvé poskytlo společnou abstraktní vrstvu pro řízení pravidel a účtování, což umožnilo PCRF konzistentně aplikovat pravidla bez ohledu na to, zda bylo UE připojeno přes LTE, HSPA nebo později i přes ne-3GPP přístup jako WiFi. To bylo zásadní pro konvergenci pevných a mobilních sítí a bezproblémový uživatelský zážitek. Za druhé formalizovalo vztah mezi relací služby uživatele (např. IMS hovorem) a podkladovým přenosovým bearerem, což umožnilo dynamické vynucování QoS na základě požadavků služby v reálném čase. To byl významný pokrok oproti statickému poskytování QoS. Konečně, definováním modelu IP-CAN relace a beareru vytvořilo čistou architekturu pro účtovací systémy, aby korelovaly využití s konkrétními službami a pravidly, čímž podpořily složité modely účtování, jako je sponzorovaný přenos dat nebo zero-rating.

## Klíčové vlastnosti

- Abstrahuje koncovou IP konektivitu od UE k bráně PDN
- Tvoří kontext pro správu pravidel Policy and Charging Control (PCC)
- Podporuje zřizování, modifikaci a ukončování IP-CAN bearerů se specifickou QoS
- Umožňuje vynucování pravidel nezávislé na přístupové technologii napříč 3GPP a ne-3GPP přístupy
- Poskytuje rámec pro účtování a evidenci zohledňující služby
- Umožňuje správu mobility a kontinuitu relace pro IP toky

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)

## Definující specifikace

- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture

---

📖 **Anglický originál a plná specifikace:** [IPCAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipcan/)
