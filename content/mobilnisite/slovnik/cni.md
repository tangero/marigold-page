---
slug: "cni"
url: "/mobilnisite/slovnik/cni/"
type: "slovnik"
title: "CNI – Critical National Infrastructure"
date: 2025-01-01
abbr: "CNI"
fullName: "Critical National Infrastructure"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cni/"
summary: "Kritická národní infrastruktura (CNI) označuje telekomunikační systémy určené jako klíčové pro národní bezpečnost, ekonomickou stabilitu a veřejnou bezpečnost. V rámci 3GPP CNI zahrnuje specializované"
---

CNI je rámec pro ochranu určených telekomunikačních systémů, které jsou klíčové pro národní bezpečnost, ekonomickou stabilitu a veřejnou bezpečnost, a zajišťuje jejich kontinuitu prostřednictvím specializovaných schopností a prioritního přístupu během krizí.

## Popis

Kritická národní infrastruktura (CNI) ve standardech 3GPP stanovuje komplexní rámec pro identifikaci, ochranu a zajištění kontinuity telekomunikačních sítí považovaných za klíčové pro národní bezpečnost, ekonomickou stabilitu a veřejnou bezpečnost. Koncept přesahuje tradiční síťovou architekturu a zahrnuje rámce politik, regulatorní požadavky a specializované technické schopnosti, které umožňují sítím udržovat provoz během mimořádných událostí, přírodních katastrof nebo bezpečnostních hrozeb. CNI zahrnuje jak fyzickou infrastrukturu (základnové stanice, uzly core sítě, přenosové linky), tak logické komponenty (databáze účastníků, autentizační systémy, směrovací protokoly), které musí zůstat funkční, aby se předešlo narušení společnosti.

Architektonická implementace CNI zahrnuje více vrstev ochrany a redundance. Na fyzické vrstvě vyžadují zařízení CNI odolné lokality se záložními zdroji energie, fyzickými bezpečnostními opatřeními a geografickou diverzitou, aby odolaly různým hrozbám. Síťová architektura zahrnuje redundantní cesty, mechanismy převzetí služeb při selhání a distribuované funkce core sítě, aby se předešlo jediným bodům selhání. Logická architektura zahrnuje specializované prioritní služby, jako je Multimedia Priority Service ([MPS](/mobilnisite/slovnik/mps/)) a Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), které zajišťují, že autorizovaní uživatelé mohou udržovat komunikaci, když jsou sítě přetížené nebo degradované. Tyto služby se integrují s rámci Policy and Charging Control (PCC) k vynucení prioritního zacházení napříč všemi síťovými doménami.

Klíčové technické komponenty implementace CNI zahrnují mechanismy prioritního přístupu, které fungují napříč doménami Radio Access Network (RAN), přenosové sítě a core sítě. V RAN dostávají uživatelé CNI prioritní přidělování rádiových prostředků prostřednictvím QoS Class Identifiers ([QCI](/mobilnisite/slovnik/qci/)) a parametrů Allocation and Retention Priority ([ARP](/mobilnisite/slovnik/arp/)), což zajišťuje, že jejich relace jsou zřízeny a udržovány i během přetížení. Core síť implementuje specializované směrování, správu relací a vynucování politik pro provoz CNI. Autentizační a autorizační systémy zahrnují vylepšené bezpečnostní protokoly a vyhrazenou správu přihlašovacích údajů pro uživatele a zařízení CNI. Síťové manažerské systémy zahrnují specializované monitorování, detekci chyb a procedury obnovy specificky navržené pro komponenty CNI.

Operační rámec pro CNI zahrnuje kontinuální monitoring, pravidelné testování a koordinované protokoly pro reakci. Operátoři sítí musí implementovat komplexní bezpečnostní opatření včetně detekce vniknutí, šifrování a řízení přístupu specificky uzpůsobených pro komponenty CNI. Dodržování regulatorních požadavků vyžaduje dokumentované procedury pro reakci na incidenty, obnovu po havárii a plánování kontinuity podnikání. Interoperabilita mezi CNI sítěmi různých operátorů je nezbytná pro národní pokrytí a vyžaduje standardizovaná rozhraní a protokoly specifikované ve specifikacích 3GPP. Rámec CNI také řeší mezistátní koordinaci pro mezinárodní mimořádné události a podporuje sdílení informací mezi vládními agenturami a operátory sítí při zachování odpovídajících bezpečnostních hranic.

## K čemu slouží

Koncept Kritické národní infrastruktury v telekomunikacích vznikl z poznání, že moderní společnosti se staly zásadně závislými na komunikačních sítích pro základní služby včetně reakce na mimořádné události, finančních transakcí, řízení energetiky a provozu vlády. Tradiční komerční sítě, optimalizované pro efektivitu a nákladovou efektivitu, často postrádaly odolnost a prioritní mechanismy potřebné během krizí, kdy sítě zažívají extrémní přetížení nebo fyzické poškození. Historické události, jako přírodní katastrofy, teroristické útoky a rozsáhlé mimořádné události, ukázaly, že bez chráněných komunikačních kanálů mohou být reakční služby ztíženy, ekonomická stabilita ohrožena a veřejná bezpečnost narušena.

CNI řeší několik kritických omezení konvenčních telekomunikačních sítí. Standardní komerční sítě typicky používají modely služeb typu best-effort, které nemohou garantovat konektivitu pro základní služby během špičkové poptávky nebo degradace sítě. Postrádají systematické mechanismy pro identifikaci a upřednostnění provozu od autorizovaného personálu pro mimořádné události, vládních agentur a operátorů kritické infrastruktury. Zranitelnosti fyzické infrastruktury, včetně centralizovaných bodů selhání a nedostatečných záložních systémů, vytvářejí rizika rozsáhlého narušení služeb. Bezpečnostní rámce v komerčních sítích se často zaměřují na ochranu příjmových toků a soukromí zákazníků spíše než na zajištění dostupnosti sítě proti koordinovaným útokům nebo extrémním scénářům.

Standardizace schopností CNI v 3GPP poskytuje konzistentní technický základ, který umožňuje interoperabilitu mezi sítěmi různých operátorů a přes národní hranice. Stanovením standardizovaných prioritních mechanismů, bezpečnostních požadavků a funkcí odolnosti 3GPP zajišťuje, že implementace CNI mohou bezproblémově fungovat během nadnárodních mimořádných událostí nebo koordinovaných reakcí. Rámec také umožňuje efektivní využití prostředků tím, že umožňuje sítím normálně provozovat při zachování rezervované kapacity a prioritních cest pro uživatele CNI, když je to potřeba. Tento vyvážený přístup předchází ekonomické neefektivitě vyhrazených paralelních sítí a zároveň zajišťuje spolehlivou komunikaci pro mimořádné události.

## Klíčové vlastnosti

- Mechanismy prioritního přístupu napříč doménami RAN a core sítě
- Vylepšené požadavky na fyzickou bezpečnost a odolnost lokalit
- Redundantní architektura s geografickou diverzitou a schopnostmi převzetí služeb při selhání
- Integrace se službami Multimedia Priority Service (MPS) a Mission Critical Services (MCS)
- Specializovaná autentizace a autorizace pro uživatele a zařízení CNI
- Komplexní monitorovací a manažerské systémy pro komponenty CNI

## Definující specifikace

- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TR 33.848** (Rel-18) — Technical Report on Virtualisation Security
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [CNI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cni/)
