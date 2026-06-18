---
slug: "v-gmlc"
url: "/mobilnisite/slovnik/v-gmlc/"
type: "slovnik"
title: "V-GMLC – Visited-Gateway Mobile Location Centre"
date: 2025-01-01
abbr: "V-GMLC"
fullName: "Visited-Gateway Mobile Location Centre"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/v-gmlc/"
summary: "Prvek jádra sítě v navštívené síti, který slouží jako brána pro požadavky na služby určení polohy cílené na roamující mobilní zařízení. Spolupracuje s místními systémy určování polohy sítě a s GMLC do"
---

V-GMLC (Visited-Gateway Mobile Location Centre) je brána pro služby určení polohy v navštívené síti, která poskytuje informace o poloze roamujících účastníků prostřednictvím rozhraní s místními systémy určování polohy a s GMLC domovské sítě.

## Popis

Visited-Gateway Mobile Location Centre (V-GMLC) je kritický funkční uzel v rámci standardizované architektury 3GPP pro služby určení polohy ([LCS](/mobilnisite/slovnik/lcs/)). Nasazuje se v navštívené veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)), když je cílové uživatelské zařízení (UE) v roamingu. V-GMLC slouží jako hlavní vstupní bod v navštívené síti pro požadavky na určení polohy pocházející od externích klientů služeb založených na poloze ([LBS](/mobilnisite/slovnik/lbs/)) nebo od domovského [GMLC](/mobilnisite/slovnik/gmlc/) ([H-GMLC](/mobilnisite/slovnik/h-gmlc/)) v domovské síti účastníka. Jeho základní rolí je řídit proces získání polohy v rámci domény navštívené sítě a zajistit splnění požadavků na ochranu soukromí, zabezpečení a regulace.

Operačně, když je přijat požadavek na určení polohy roamujícího účastníka (často směrovaný přes H-GMLC), V-GMLC vykonává několik klíčových funkcí. Nejprve ověří platnost požadavku vůči místním politikám a může komunikovat s domovským registrem polohy ([HLR](/mobilnisite/slovnik/hlr/)) nebo serverem předplatitelů ([HSS](/mobilnisite/slovnik/hss/)) pro autorizaci účastníka. Následně V-GMLC vybere vhodnou metodu určování polohy na základě požadované kvality služby (QoS), jako je Cell-ID, [OTDOA](/mobilnisite/slovnik/otdoa/) nebo asistovaný GNSS (A-GNSS). Poté komunikuje s prvky jádra navštívené sítě, především s mobilní ústřednou (MSC) nebo s Mobility Management Entity (MME)/Access and Mobility Management Function (AMF), které následně zapojí rádiový přístupový síť a potenciálně i samotné UE, aby získaly měření pro určení polohy.

Jakmile je odhad polohy vypočítán (buď v síti, nebo v UE), je výsledek doručen zpět do V-GMLC. V-GMLC je odpovědný za formátování tohoto výsledku, který může zahrnovat zeměpisnou šířku, délku, nadmořskou výšku a odhady přesnosti, do standardizované podoby. Následně směruje odpověď s polohou zpět k původnímu žadateli, typicky k H-GMLC, který ji následně doručí externímu LCS klientovi. V-GMLC také zajišťuje generování účtovacích datových záznamů (CDR) za transakci určení polohy provedenou v navštívené síti, což je zásadní pro vypořádání mezi operátory. Jeho architektura zajišťuje, že navštívená síť udržuje kontrolu nad svými prostředky pro určování polohy a daty účastníků, a přitom spolupracuje s domovskou sítí, aby poskytla roamujícím uživatelům bezproblémový zážitek ze služeb LCS.

## K čemu slouží

V-GMLC byl zaveden, aby umožnil zákonné a komerční služby založené na poloze (LCS) pro účastníky, když se pohybují mimo svou domovskou síť. Před jeho standardizací bylo poskytování polohy roamujícího uživatele složité a nestandardizované, často vyžadující přímá proprietární rozhraní mezi operátory nebo omezující služby pouze na pokrytí domovské sítě. To bylo nedostatečné pro nouzové služby (např. E112/E911), které vyžadují spolehlivé určení polohy bez ohledu na síť, a pro komerční aplikace, jako je sledování vozového parku nebo reklama založená na poloze, které musí fungovat bezproblémově přes hranice.

Jeho vytvoření ve vydání 6 jako součást zralé architektury LCS vyřešilo kritický problém řízení přístupu a správy síťových zdrojů v roamingu. V-GMLC umožňuje operátorovi navštívené sítě ověřovat a autorizovat požadavky na určení polohy, čímž chrání soukromí účastníků a zajišťuje soulad s místními předpisy. Také umožňuje navštívenému operátorovi využívat vlastní, potenciálně přesnější, infrastrukturu pro určování polohy a účtovat za použití svých síťových zdrojů. Definováním jasné bránové funkce v navštívené síti vytvořil 3GPP škálovatelný, bezpečný a interoperabilní model pro globální LCS, který se stal základem pro nouzové služby, služby s přidanou hodnotou a nástroje pro optimalizaci sítí po celém světě.

## Klíčové vlastnosti

- Brána pro požadavky na určení polohy cílené na roamující účastníky
- Autorizace požadavků na určení polohy na základě profilů ochrany soukromí účastníka
- Interakce s jádrem navštívené sítě (MSC/MME/AMF) a systémy určování polohy
- Podpora více metod určování polohy (např. Cell-ID, OTDOA, A-GNSS)
- Generování účtovacích datových záznamů (CDR) za využití navštívené sítě
- Bezpečná spolupráce s domovským GMLC (H-GMLC) prostřednictvím standardizovaných rozhraní

## Související pojmy

- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 29.173** (Rel-19) — Diameter-based SLh Interface for LCS
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [V-GMLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-gmlc/)
