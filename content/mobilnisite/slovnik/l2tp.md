---
slug: "l2tp"
url: "/mobilnisite/slovnik/l2tp/"
type: "slovnik"
title: "L2TP – Layer Two Tunneling Protocol"
date: 2025-01-01
abbr: "L2TP"
fullName: "Layer Two Tunneling Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/l2tp/"
summary: "Tunelovací protokol odvozený od IETF, používaný v sítích 3GPP pro přenos paketů vrstvy 2 (např. PPP rámců) po IP sítích. Primárně se používá v bráně paketové datové sítě (PGW/PGW-U) k zřizování tunelů"
---

L2TP je tunelovací protokol používaný v sítích 3GPP pro přenos paketů vrstvy 2 po IP, primárně v PGW pro zřizování tunelů pro uživatelská data k externím paketovým datovým sítím.

## Popis

Layer Two Tunneling Protocol (L2TP) je standardizovaný tunelovací protokol, původně definovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 2661, později aktualizovaný), který je přijat a odkazován ve specifikacích 3GPP pro konkrétní rozhraní. V architektuře 3GPP se L2TPv2 používá primárně na rozhraní SGi (mezi bránou paketové datové sítě – [PGW](/mobilnisite/slovnik/pgw/) a externí paketovou datovou sítí) a v rámci nastavení připojení k paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/)). Poskytuje mechanismus pro tunelování rámců Point-to-Point Protocol ([PPP](/mobilnisite/slovnik/ppp/)) nebo jiného provozu vrstvy 2 po IP síti, čímž vytváří virtuální point-to-point spojení.

L2TP funguje tak, že naváže řídicí spojení a jednu nebo více relací v rámci tohoto spojení. Koncovými body jsou L2TP Access Concentrator ([LAC](/mobilnisite/slovnik/lac/)) a L2TP Network Server ([LNS](/mobilnisite/slovnik/lns/)). V kontextu 3GPP vystupuje uživatelské zařízení (UE) jako PPP protistrana, PGW často zahrnuje funkci LNS a externí broadband network server (BNS) nebo podniková síť UE může vystupovat jako LAC. Protokol zapouzdřuje původní PPP rámce do paketů L2TP, které jsou následně dále zapouzdřeny v [UDP](/mobilnisite/slovnik/udp/)/IP pro přenos přes síť. Tím se vytváří bezpečné, logické rozšíření sítě vrstvy 2 přes IP infrastrukturu.

Klíčové komponenty v rámci 3GPP zahrnují výměnu L2TP řídicích zpráv pro zřizování, správu a ukončování tunelů/relací a proces datového zapouzdření. Jeho role je klíčová pro určité typy připojení k PDN, zejména pro propojení se staršími vytáčenými sítěmi, poskytování přístupu k virtuální privátní síti (VPN) pro uživatele nebo pro specifické scénáře konvergence pevných a mobilních sítí. Umožňuje mobilním operátorům nabízet bezproblémový zabezpečený přístup k podnikovým sítím nebo službám ISP rozšířením tradiční vytáčené nebo širokopásmové PPP relace přes mobilní páteřní síť.

## K čemu slouží

L2TP byl do specifikací 3GPP začleněn, aby řešil problém poskytování vzdáleného, ověřeného síťového přístupu přes IP páteřní sítě. V raných vydáních 3GPP (Rel-4/5) existovala potřeba podporovat propojení se stávajícími infrastrukturami poskytovatelů internetových služeb (ISP), které se silně spoléhaly na PPP pro ověřování uživatelů (jako CHAP/PAP) a přiřazování IP adres. L2TP poskytl standardizovaný způsob tunelování těchto PPP relací z UE přes mobilní paketovou páteřní síť k síťovému serveru ISP.

Jeho vznik byl motivován přechodem od přepojování okruhů (kde mělo UE přímé modemové spojení) k paketově přepínaným páteřním sítím. Jednoduché posílání syrového PPP přes síť GPRS nebylo proveditelné. L2TP to řešil definováním robustního tunelovacího mechanismu, který dokáže procházet zařízeními pro překlad síťových adres (NAT) (pomocí UDP), poskytovat vlastní zajištění pořadí a doručení a oddělovat řídicí a datovou rovinu. Umožnil operátorům využít stávající systémy AAA (Authentication, Authorization, Accounting) a účtování vytvořené pro vytáčené PPP uživatele.

Zatímco novější, více integrované metody ověřování jako EAP se staly převládajícími pro přímý mobilní přístup, L2TP zůstává relevantní pro specifické případy použití vyžadující transparentní ukončení tunelu vrstvy 2 mimo síť mobilního operátora, jako jsou určité typy podnikových VPN nebo integrace starších služeb, čímž poskytuje most mezi moderními mobilními IP architekturami a tradičními síťovými přístupovými servery.

## Klíčové vlastnosti

- Tunelování PPP rámců po IP sítích (UDP port 1701)
- Samostatné řídicí spojení pro správu tunelu/relace a datové relace pro uživatelský provoz
- Podpora ověřování a zabezpečení tunelu (pomocí AVP a volitelného IPsec)
- Schopnost procházet zařízeními NAT díky zapouzdření v UDP
- Mechanismy pro řízení toku, zpracování chyb a keep-alive relace
- Používá se pro specifické typy PDN (např. pro rozhraní s externími sítěmi ISP) v 3GPP

## Související pojmy

- [PPP – Priority Precedence Preemption](/mobilnisite/slovnik/ppp/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [L2TP na 3GPP Explorer](https://3gpp-explorer.com/glossary/l2tp/)
