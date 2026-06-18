---
slug: "bras"
url: "/mobilnisite/slovnik/bras/"
type: "slovnik"
title: "BRAS – Broadband Remote Access Server"
date: 2025-01-01
abbr: "BRAS"
fullName: "Broadband Remote Access Server"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bras/"
summary: "Broadband Remote Access Server (BRAS), známý také jako Broadband Network Gateway (BNG), je síťový prvek agregující relace účastníků ze širokopásmových přístupových sítí. Funguje jako brána mezi přístu"
---

BRAS je síťová brána, která agreguje relace účastníků z širokopásmových přístupových sítí a zajišťuje autentizaci, správu IP adres a vynucování politik mezi přístupovou a jádrovou sítí.

## Popis

Broadband Remote Access Server (BRAS) je ústřední agregační a řídicí bod v síti poskytovatele služeb, umístěný na okraji jádrové IP sítě. Jeho primární rolí je ukončovat a spravovat relace účastníků pocházející z různých širokopásmových přístupových technologií, jako je Digital Subscriber Line ([DSL](/mobilnisite/slovnik/dsl/)), pasivní optické sítě ([PON](/mobilnisite/slovnik/pon/)) nebo přístup založený na Ethernetu. Z architektonického hlediska se BRAS nachází mezi přístupovou sítí (např. DSLAMy, OLT) a směrovači jádrové sítě a představuje první IP-aware uzel pro provoz účastníka. Navazuje relace Point-to-Point Protocol ([PPP](/mobilnisite/slovnik/ppp/)) nebo IP over Ethernet (IPoE) s koncovým zařízením účastníka ([CPE](/mobilnisite/slovnik/cpe/)) a zajišťuje celý životní cyklus od zahájení do ukončení relace.

Provozně BRAS plní několik klíčových funkcí. Při navazování relace komunikuje se servery [AAA](/mobilnisite/slovnik/aaa/) (obvykle pomocí protokolů [RADIUS](/mobilnisite/slovnik/radius/) nebo Diameter) za účelem autentizace účastníků a autorizace jejich služebních profilů. Přiřazuje účastníkům IP adresy, ať už z lokálních pulů nebo prostřednictvím interakce se serverem Dynamic Host Configuration Protocol ([DHCP](/mobilnisite/slovnik/dhcp/)). Základní funkcí je vynucování politik, kde BRAS aplikuje pravidla definovaná v profilu účastníka nebo pocházející z funkce Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)). Tato pravidla řídí šířku pásma, parametry QoS (např. priorizaci a tvarování provozu) a přístupové seznamy (ACL), což umožňuje vytvářet vrstvené služební plány (např. základní, prémiové, pro podniky). BRAS také provádí podrobné účtování, sbírá údaje o délce relace, objemu přenesených dat a další metriky pro fakturaci a analýzu sítě.

Z hlediska přeposílání provozu BRAS směruje provoz účastníků do příslušné služební sítě nebo na veřejný internet. Často implementuje Network Address Translation (NAT) pro privátní IPv4 adresy a může podporovat přechodové mechanismy pro IPv6. Pokročilé platformy BRAS integrují možnosti deep packet inspection (DPI) pro lepší povědomí o službách a řízení politik na základě aplikací. V kontextu 3GPP je BRAS/BNG zmíněn ve specifikacích pro propojení s fixním širokopásmovým přístupem, kde je jeho role v QoS a řízení politik sladěna s architekturou PCC (Policy and Charging Control), což umožňuje jednotnou správu politik napříč fixními a mobilními sítěmi. Jeho rozhraní pro správu podporují konfiguraci, správu poruch a sledování výkonu jako součást OSS/BSS operátora.

## K čemu slouží

BRAS byl vytvořen, aby řešil základní výzvy škálování a správy rozsáhlých sítí širokopásmových účastníků. Když technologie DSL a další širokopásmové technologie překročily rámec jednoduchého připojení k internetu a začaly nabízet diferenciované služby (jako VoIP, IPTV a hraní her), potřebovali síťoví operátoři centralizovaný řídicí bod na okraji sítě. Předchozí přístupy využívající jednoduché směrovače nebo přepínače vrstvy 2 postrádaly podrobné povědomí o účastnících, robustní integraci AAA a sofistikované vynucování politik potřebné pro komerční poskytování služeb. BRAS tento problém vyřešil tím, že poskytl vyhrazený síťový prvek, který dokáže na jediném fyzickém rozhraní jednoznačně identifikovat a spravovat tisíce individuálních relací účastníků.

Historicky byl jeho vývoj hnacím motorem masové nasazení DSL na konci 90. let a na počátku 21. století. Operátoři potřebovali způsob, jak agregovat nesčetné individuální PPP relace z DSL modemů, autentizovat je vůči databázi účastníků, dynamicky přidělovat IP adresy a aplikovat služebně specifické politiky. BRAS se stal základním kamenem pro přeměnu surové širokopásmové přístupové infrastruktury na spravovatelnou, fakturovatelnou a na služby bohatou síť. Umožnil obchodní model vrstvených internetových služeb a připravil cestu pro triple-play nabídky (data, hlas, video).

V ekosystému 3GPP bylo formální uznání a specifikace funkcí BRAS/BNG, zejména ve vydáních pokrývajících fixní širokopásmový přístup a konvergenci (FMC), motivováno potřebou bezproblémového propojení mezi mobilními a fixními sítěmi. Definováním způsobu interakce BRAS s řídicími (PCRF) a autentizačními rámci definovanými 3GPP umožňují standardy 3GPP operátorům poskytovat konzistentní uživatelské zážitky a jednotnou správu politik napříč všemi typy přístupu, čímž řeší omezení izolovaného síťového managementu.

## Klíčové vlastnosti

- Agregace a ukončení relací účastníků (PPP, IPoE)
- Autentizace, autorizace a účtování (AAA) prostřednictvím RADIUS/Diameter
- Dynamické přidělování (DHCP, lokální puly) a správa IP adres
- Vynucování politik a účtování (sladěno s architekturou 3GPP PCC)
- Vynucování kvality služeb (QoS) (tvarování provozu, priorizace, policování)
- Povědomé o účastníkovi směrování a Network Address Translation (NAT)

## Definující specifikace

- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.839** (Rel-12) — Fixed-Mobile Convergence Architecture Study
- **TS 23.896** (Rel-12) — Policy & Charging Control for Fixed Broadband Convergence
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.819** (Rel-7) — IMS Services via Fixed Broadband Access
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study

---

📖 **Anglický originál a plná specifikace:** [BRAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bras/)
