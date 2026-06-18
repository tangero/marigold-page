---
slug: "wag"
url: "/mobilnisite/slovnik/wag/"
type: "slovnik"
title: "WAG – Wireless Access Gateway"
date: 2025-01-01
abbr: "WAG"
fullName: "Wireless Access Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wag/"
summary: "Wireless Access Gateway (WAG) je prvek základnové sítě, který zajišťuje bezpečnou a řízenou interoperabilitu mezi mobilními sítěmi 3GPP a ne-3GPP IP přístupovými sítěmi, jako jsou WLAN. Funguje jako b"
---

WAG je brána v základnové síti, která zajišťuje bezpečnou interoperabilitu a řízené směrování mezi mobilními sítěmi 3GPP a ne-3GPP IP přístupovými sítěmi, jako jsou WLAN.

## Popis

Wireless Access Gateway (WAG) je standardizovaná síťová funkce definovaná konsorciem 3GPP, která usnadňuje bezpečný a řízený přístup z ne-3GPP IP sítí, především bezdrátových lokálních sítí ([WLAN](/mobilnisite/slovnik/wlan/)), do základnové sítě 3GPP. Z architektonického hlediska se nachází na hranici mezi nedůvěryhodnou ne-3GPP IP přístupovou sítí a důvěryhodným jádrem 3GPP, často rozhraním s Packet Data Gateway ([PDG](/mobilnisite/slovnik/pdg/)) pro tunelování uživatelské roviny provozu. Primární funkcí WAG je vynucování přístupové kontroly založené na politikách. Autentizuje a autorizuje uživatelské zařízení (UE), které se pokouší přistoupit ke službám 3GPP přes hotspot WLAN, typicky pomocí metod Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/)) přes referenční bod Ww. Tento proces zahrnuje interakci s infrastrukturou 3GPP [AAA](/mobilnisite/slovnik/aaa/) (Authentication, Authorization, and Accounting), včetně Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), pro ověření přihlašovacích údajů účastníka a jeho služebního profilu.

Z pohledu datové roviny WAG neukončuje uživatelský IP provoz, ale funguje spíše jako vynucovací bod. Zajišťuje, že pouze autorizovaný provoz od autentizovaných UE je směrován směrem k PDG, které s UE vytváří [IPsec](/mobilnisite/slovnik/ipsec/) tunel (pomocí IKEv2) pro bezpečný přenos dat. WAG může provádět filtrování paketů, policing a směrování na základě politik přijatých ze serveru AAA. Tato architektura, definovaná v raných verzích 3GPP pro interoperabilitu s WLAN, vytváří jasnou demarkační linii: WAG zajišťuje řízení přístupu a počáteční směrování na okraji sítě, zatímco PDG se stará o zabezpečené tunelování a připojení k externím paketovým datovým sítím ([PDN](/mobilnisite/slovnik/pdn/)).

Role WAG je nedílnou součástí System Architecture Evolution ([SAE](/mobilnisite/slovnik/sae/)) konsorcia 3GPP pro ne-3GPP přístup. Podporuje mobilní scénáře, umožňující UE objevit a vybrat WAG pro přístup. Zatímco pozdější architektury se vyvinuly se zavedením ePDG pro nedůvěryhodný ne-3GPP přístup v EPS a Non-3GPP Interworking Function (N3IWF) v 5GS, koncept WAG položil základní principy specializované brány pro správu a zabezpečení vstupního bodu z externích bezdrátových sítí do mobilního jádra, čímž zajišťuje kontrolu operátora nad přístupem ke službám a jeho zabezpečením.

## K čemu slouží

WAG byl vytvořen, aby řešil rostoucí potřebu mobilních operátorů integrovat hotspoty WLAN se svými celulárními sítěmi řízeným a bezpečným způsobem. Na počátku 21. století nabízely WLAN vysokou přenosovou kapacitu, ale postrádaly integrované rámce pro autentizaci, účtování a zabezpečení, které jsou typické pro celulární sítě. Účelem WAG bylo poskytnout standardizovanou bránu, která by mohla začlenit přístup přes WLAN pod kontrolu operátora, což by umožnilo nové obchodní modely, jako je plynulé odlehčování provozu a jednotné nabídky služeb.

Před jeho standardizací představovala ad-hoc integrace WLAN významné problémy: neexistovala standardizovaná metoda, jak by se účastník celulární sítě mohl přihlásit ke WLAN pomocí přihlašovacích údajů ze SIM karty, nebylo zajištěno zabezpečení přístupového spoje a operátor nemohl uplatňovat jednotné politiky a účtování. WAG tyto problémy vyřešil definicí jasné architektonické komponenty, která komunikovala s existující infrastrukturou 3GPP AAA. To umožnilo operátorům využívat svou databázi účastníků (HSS) pro autentizaci přes WLAN a jednotně vynucovat přístupové politiky bez ohledu na rádiovou technologii.

Jeho vytvoření bylo motivováno snahou o konvergenci sítí a kontinuitu služeb. Umožnil scénáře, kdy uživatel mohl zahájit datovou relaci v celulární síti a po vstupu do oblasti pokrytí WLAN mohla být jeho relace bezpečně předána nebo odlehčena, přičemž operátor zachovával přehled a kontrolu. WAG standardizoval kritický první krok z nedůvěryhodné, ne-3GPP sítě do důvěryhodného jádra, čímž vytvořil model zabezpečení a vynucování politik, který se později vyvinul pro další typy přístupu v sítích 4G a 5G.

## Klíčové vlastnosti

- Zajišťuje interoperabilitu s 3GPP AAA pro autentizaci a autorizaci účastníka
- Poskytuje vynucování politik na okraji ne-3GPP IP přístupových sítí
- Směruje autorizovaný uživatelský provoz směrem k Packet Data Gateway (PDG)
- Podporuje funkce pro objevování přístupové sítě a její výběr
- Umožňuje bezpečné odlehčování provozu přes WLAN pro účastníky 3GPP
- Umožňuje operátorem řízené účtování a charging za přístup přes WLAN

## Související pojmy

- [PDG – Packet Data Gateway](/mobilnisite/slovnik/pdg/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)

## Definující specifikace

- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 28.601** (Rel-12) — Telecom management; CN and non-3GPP access NRM IRP Requirements
- **TS 28.602** (Rel-12) — CN & non-3GPP NRM IRP Information Service
- **TS 29.234** (Rel-11) — WLAN-3GPP Interworking Stage-3 Protocol
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 32.820** (Rel-8) — Charging Architecture Study for Evolved 3GPP
- **TS 33.234** (Rel-19) — 3GPP-WLAN Interworking Security

---

📖 **Anglický originál a plná specifikace:** [WAG na 3GPP Explorer](https://3gpp-explorer.com/glossary/wag/)
