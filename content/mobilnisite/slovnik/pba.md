---
slug: "pba"
url: "/mobilnisite/slovnik/pba/"
type: "slovnik"
title: "PBA – Proxy Binding Acknowledgment"
date: 2025-01-01
abbr: "PBA"
fullName: "Proxy Binding Acknowledgment"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pba/"
summary: "Zpráva zaslaná kotvou místní mobility (LMA) v síti PMIPv6 bráně mobilního přístupu (MAG) k potvrzení úspěšné registrace nebo aktualizace vazby pro mobilní uzel. Je to klíčová součást signalizace pro z"
---

PBA je zpráva Proxy Binding Acknowledgment (potvrzení proxy vazby) zaslaná LMA MAG v síti PMIPv6, která potvrzuje úspěšnou registraci nebo aktualizaci vazby pro mobilní uzel.

## Popis

Proxy Binding Acknowledgment (PBA) je protokolová zpráva definovaná v rámci architektury Proxy Mobile IPv6 (PMIPv6), specifikovaná v 3GPP TS 29.275. Jedná se o odpověď generovanou kotvou místní mobility ([LMA](/mobilnisite/slovnik/lma/)) a zaslanou bráně mobilního přístupu ([MAG](/mobilnisite/slovnik/mag/)) jako reakci na zprávu Proxy Binding Update ([PBU](/mobilnisite/slovnik/pbu/)). Zpráva PBA slouží k potvrzení přijetí a zpracování žádosti o vazbu pro konkrétní mobilní uzel ([MN](/mobilnisite/slovnik/mn/)) ze strany LMA. Hlavní funkcí PBA je vytvořit nebo aktualizovat záznam vázací cache na LMA, který asociuje prefix domácí sítě ([HNP](/mobilnisite/slovnik/hnp/)) nebo domácí adresu mobilního uzlu s proxy care-of adresou (Proxy-CoA) MAG. Tato vazba umožňuje LMA tunelovat pakety určené pro MN na správnou MAG, která je následně lokálně doručí MN.

Zpráva PBA obsahuje několik povinných a volitelných možností hlavičky mobility, které přenášejí zásadní informace. Nejvýznamnější je možnost Home Network Prefix, která přiděluje mobilnímu uzlu prefix nebo adresu pro použití v přístupové síti, čímž vytváří iluzi permanentní domácí linky. Mezi další důležité možnosti patří pole stavu Binding Acknowledgement, udávající úspěch nebo selhání (např. úspěch, proxy registrace není povolena), a sekvenční číslo pro spárování PBA s odpovídající PBU. Po přijetí úspěšného PBA MAG vytvoří obousměrný tunel s LMA a propaguje přidělený prefix mobilnímu uzlu, což umožňuje MN nakonfigurovat si svou IP adresu a udržovat běžící relace bez povědomí o síťově řízené správě mobility.

V rámci architektury 3GPP Evolved Packet Core (EPC) se PMIPv6 používá jako jeden z protokolů pro rozhraní S5/S8 mezi Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)), kde PGW funguje jako LMA a SGW jako MAG. V tomto kontextu je zpráva PBA klíčová pro zřízení [GTP](/mobilnisite/slovnik/gtp/) nebo PMIPv6 tunelu pro uživatelská data, když se UE připojuje k síti nebo provádí předání. Zajišťuje, že PGW správně směruje downlinkový provoz na obsluhující SGW. Spolehlivá a včasná výměna zpráv PBU a PBA je zásadní pro plynulou mobilitu, kontinuitu relací a efektivní směrování paketů ve scénářích síťově řízené mobility a tvoří základ signalizace řídicí roviny v nasazeních založených na PMIPv6.

## K čemu slouží

Zpráva PBA byla vytvořena jako součást protokolu PMIPv6 k řešení potřeby síťově řízené správy IP mobility bez nutnosti klientského mobilního softwaru. Tradiční hostitelsky řízené protokoly mobility, jako je Mobile IPv6, vyžadují, aby se mobilní uzel sám zapojoval do signalizace se svým domácím agentem, což může být složité a energeticky neefektivní pro zařízení s omezenými zdroji. PMIPv6, a tím i PBA, přesouvá zátěž správy mobility na síťovou infrastrukturu (LMA a MAG). To umožňuje jakémukoli zařízení s podporou IP, dokonce i bez specifické podpory mobility, zažívat plynulá předání a kontinuitu relací při pohybu mezi přístupovými body spravovanými sítí.

Vytvoření PBA bylo motivováno potřebou spolehlivého mechanismu potvrzení v rámci signalizační sady PMIPv6. MAG iniciuje správu mobility jménem MN odesláním PBU. PBA od LMA poskytuje nezbytné potvrzení a parametry (jako je prefix domácí sítě) k dokončení zřízení relace. Bez tohoto potvrzení si MAG nemůže být jistá, že byla vazba na LMA vytvořena, což by mohlo vést k potenciálním selháním směrování. V kontextu sítí 3GPP přijetí PMIPv6 pro určitá rozhraní poskytlo standardizovanou, IP-based alternativu k GTP a PBA se stala klíčovým prvkem řídicí roviny pro správu tunelů a ukotvení IP adresy UE, čímž podpořila všeo-IP vizi Evolved Packet System.

## Klíčové vlastnosti

- Potvrzuje úspěšné zpracování zprávy Proxy Binding Update (PBU) od MAG.
- Nese přidělený prefix domácí sítě (HNP) pro mobilní uzel.
- Obsahuje pole stavu udávající úspěch nebo konkrétní chybové stavy.
- Obsahuje sekvenční číslo pro spárování žádostí a potvrzení.
- Vytváří záznam vázací cache na LMA spojující identitu MN s adresou MAG.
- Spouští zřízení obousměrného tunelu mezi LMA a MAG pro přeposílání dat.

## Související pojmy

- [PBU – Proxy Binding Update](/mobilnisite/slovnik/pbu/)
- [LMA – Local Mobility Anchor](/mobilnisite/slovnik/lma/)
- [MAG – Mobility Access Gateway](/mobilnisite/slovnik/mag/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3

---

📖 **Anglický originál a plná specifikace:** [PBA na 3GPP Explorer](https://3gpp-explorer.com/glossary/pba/)
