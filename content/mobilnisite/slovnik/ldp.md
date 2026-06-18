---
slug: "ldp"
url: "/mobilnisite/slovnik/ldp/"
type: "slovnik"
title: "LDP – Label Distribution Protocol"
date: 2025-01-01
abbr: "LDP"
fullName: "Label Distribution Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ldp/"
summary: "Protokol definovaný IETF (RFC 5036) a referencovaný 3GPP pro distribuci štítků v sítích MPLS (Multi-Protocol Label Switching). Umožňuje směrovačům vytvářet cesty přepínané podle štítků (LSPs) výměnou"
---

LDP je protokol IETF používaný v sítích 3GPP MPLS pro distribuci štítků mezi směrovači, což umožňuje vytváření cest přepínaných podle štítků (Label Switched Paths) pro správu provozu (traffic engineering) a řízení přenosu.

## Popis

Protokol pro distribuci štítků (Label Distribution Protocol, LDP) je základním protokolem řídicí roviny v sítích [MPLS](/mobilnisite/slovnik/mpls/), standardizovaným [IETF](/mobilnisite/slovnik/ietf/) v [RFC](/mobilnisite/slovnik/rfc/) 5036. Ačkoli není protokolem původním od 3GPP, je v rámci specifikací 3GPP (např. 23.207 o QoS, 23.802 o vylepšeních architektury pro přenos) referencován a využíván pro správu přenosové vrstvy, která tvoří základ mobilní jádrové sítě. Primární funkcí LDP je automatické vytváření a údržba cest přepínaných podle štítků (LSPs), které mapují informace o směrování IP na štítky v přenosové rovině, což umožňuje efektivní přeposílání paketů prostřednictvím MPLS cloudu.

LDP pracuje mezi směrovači přepínajícími podle štítků (LSRs). Funguje tak, že vytváří LDP relace mezi sousedními [LSR](/mobilnisite/slovnik/lsr/) (LDP partnery). V rámci těchto relací si LSR vyměňují zprávy pro inzerování, vyžádání a uvolnění mapování štítků. Základní proces začíná tím, že každý LSR spustí svůj směrovací protokol IP (jako OSPF nebo IS-IS) pro vytvoření směrovací tabulky. LDP pak používá koncept třídy ekvivalence přenosu (Forwarding Equivalence Class, [FEC](/mobilnisite/slovnik/fec/)), typicky odpovídající IP prefixu, k seskupení paketů, které mají být přeneseny stejným způsobem. Každý LSR nezávisle naváže lokální štítek na FEC pro svůj příchozí směr. Toto navázání pak distribuuje svým LDP partnerům. Prostřednictvím této distribuované výměny je vytvořena kompletní koncová [LSP](/mobilnisite/slovnik/lsp/), kde každý skok nahradí příchozí štítek za odchozí štítek.

V systému 3GPP je LDP zvláště relevantní v kontextu přenosu v IP multimediální podsystému (IMS) a v Evolved Packet Core (EPC). Například v rámci IMS lze LDP použít k nastavení MPLS LSP mezi uzly [P-CSCF](/mobilnisite/slovnik/p-cscf/), [I-CSCF](/mobilnisite/slovnik/i-cscf/) a S-CSCF, aby bylo zajištěno přenosové spojení s garantovanou QoS pro signalizaci SIP a mediální toky podle pravidel Policy and Charging Control (PCC). Umožňuje přenosové síti poskytovat možnosti správy provozu (Traffic Engineering, TE), směrování různých tříd provozu (např. hlas, signalizace, uživatelská data) po specifických cestách s vyhrazenými prostředky. LDP spolu se svými rozšířeními, jako je CR-LDP (Constraint-Based Routing LDP), nebo ve spojení s RSVP-TE, poskytuje síťovým operátorům detailní kontrolu nad provozem v páteřní síti, který podporuje mobilní služby.

## K čemu slouží

LDP byl vytvořen k řešení problému škálovatelné a efektivní distribuce štítků v čistě IP sítích MPLS, jako alternativa k manuální konfiguraci nebo využívání jiných protokolů. Před LDP a podobnými protokoly bylo vytváření LSPs těžkopádné. Motivací byla automatizace vytváření LSPs v přímé korelaci se základním směrováním IP, což umožnilo, aby byla síť MPLS "řízena směrováním". Tato automatizace je klíčová pro rozsáhlé sítě operátorů, včetně těch, které tvoří základ systémů 3GPP.

3GPP odkazuje na LDP, aby využilo výhod MPLS v mobilním přenosu (backhaul) a přenosu jádra sítě. Tradiční mobilní přenos využíval TDM/ATM, kterému chyběla flexibilita. Přechod na čistě IP přenos vyžadoval mechanismy pro izolaci provozu, záruky QoS a efektivní přeposílání – což jsou všechny silné stránky MPLS. LDP poskytuje standardizovaný řídicí protokol k realizaci těchto výhod MPLS. Řeší omezení použití prostého směrování IP v přenosové síti, které nebere v úvahu omezení šířky pásma nebo cesty specifické pro služby. Použitím LDP (a jeho rozšíření s omezeními) mohou architektury 3GPP zajistit, že provoz řídicí roviny s vysokou prioritou (např. S1-MME, Diameter) nebo provoz uživatelské roviny v reálném čase získají vyhrazenou, spolehlivou cestu sítí, čímž se zvyšuje celková kvalita služeb a možnosti správy sítě. Jeho použití od 3GPP R99 odráží časné přijetí IP/MPLS ve vývoji jádrové sítě.

## Klíčové vlastnosti

- Distribuce štítků řízená směrováním: Vytváří LSPs na základě existující topologie směrování IP, což zjednodušuje provoz sítě.
- Protokol typu peer-to-peer: Používá přímé TCP relace mezi LSR pro spolehlivou výměnu zpráv o mapování štítků.
- Třída ekvivalence přenosu (Forwarding Equivalence Class, FEC): Seskupuje pakety určené ke stejnému koncovému bodu a zacházení, což tvoří základ pro navázání štítku.
- Režimy inzerce štítků: Podporuje jak režim Downstream Unsolicited (DU), tak Downstream on Demand (DoD) pro flexibilní provoz.
- Spolehlivost relace: Zahrnuje mechanismy pro inicializaci relace, keepalive a řádné oznamování chyb.
- Základ pro služby MPLS: Umožňuje základní jednosměrné přeposílání MPLS, což je stavební kámen pro pokročilejší služby, jako jsou VPN (L3VPN) používané v mobilním jádru sítě.

## Související pojmy

- [MPLS – Multiprotocol Label Switching Architecture](/mobilnisite/slovnik/mpls/)

## Definující specifikace

- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture

---

📖 **Anglický originál a plná specifikace:** [LDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ldp/)
