---
slug: "wsp"
url: "/mobilnisite/slovnik/wsp/"
type: "slovnik"
title: "WSP – Web Service Provider"
date: 2025-01-01
abbr: "WSP"
fullName: "Web Service Provider"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wsp/"
summary: "Entita, jak je definována protokolem Location Application Protocol (LAP), která poskytuje webové služby, často služby založené na poloze (LBS), koncovým uživatelům nebo jiným síťovým entitám. Působí j"
---

WSP je entita, která poskytuje webové služby, často služby založené na poloze, koncovým uživatelům nebo jiným síťovým entitám v rámci architektury služeb 3GPP.

## Popis

Web Service Provider (WSP) je logická role definovaná v kontextu specifikací 3GPP pro servisní architektury, zejména těch souvisejících s přidanými službami, jako jsou Location Services ([LCS](/mobilnisite/slovnik/lcs/)) a Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)). Dle specifikací jako TS 23.140 (Multimedia Messaging Service (MMS)) a TS 23.057 (Location Services (LCS)) je WSP entitou na aplikační úrovni, která hostuje a poskytuje služby, často prostřednictvím [HTTP](/mobilnisite/slovnik/http/) nebo jiných webových protokolů, klientům. Je klíčovou součástí servisní vrstvy, která komunikuje s jádrem sítě za účelem vyžádání síťových schopností, jako je poloha uživatele nebo přenos zpráv.

Architektonicky se WSP nachází mimo důvěryhodnou hranici sítě 3GPP, ale s ní komunikuje prostřednictvím standardizovaných bran a rozhraní. Pro Location Services by WSP komunikoval s Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) přes rozhraní Le, aby požádal o polohu cílového uživatele. Pro MMS může WSP komunikovat s MMSC (Multimedia Messaging Service Centre). WSP implementuje servisní logiku, uživatelská rozhraní a aplikační servery, které využívají síťové enablery. Jeho činnost zahrnuje odesílání servisních požadavků (např. požadavek na polohu), přijímání odpovědí ze sítě a zpracování těchto dat za účelem poskytnutí výsledné služby koncovému uživateli nebo korporátnímu klientovi.

Klíčové komponenty ve vztahu k WSP zahrnují prvky jádra sítě 3GPP (jako GMLC, [HSS](/mobilnisite/slovnik/hss/), MMSC), standardizovaná otevřená rozhraní (Le, Mm1) a vlastní aplikační servery WSP. Jeho role spočívá v využívání standardizovaných síťových schopností k vytváření prodejných služeb, což umožňuje ekosystém, kde poskytovatelé třetích stran mohou nabízet inovativní aplikace. Zabezpečení interakcí mezi WSP a sítí 3GPP se řídí specifikacemi jako TS 33.980, která detailně popisuje bezpečnostní požadavky pro služby založené na poloze.

## K čemu slouží

Koncept Web Service Provider byl formalizován, aby umožnil a reguloval poskytování přidaných služeb entitami externími vůči mobilnímu operátorovi. To bylo hnací silou odklonu průmyslu směrem k otevřeným servisním architekturám na počátku 2000. let, kdy operátoři usilovali o bezpečné zpřístupnění síťových schopností třetím stranám za účelem podpory inovací a vytvoření nových zdrojů příjmů. Předchozí přístupy často uzamykaly služby uvnitř uzavřeného prostředí operátora, což omezovalo jejich rozmanitost a růst.

Role WSP konkrétně řeší problém, jak bezpečně a spolehlivě umožnit externím aplikačním poskytovatelům přístup k citlivým síťovým funkcím, jako je poloha účastníka. Řeší to definováním jasné architektonické role, standardizovaných rozhraní (jako rozhraní Le pro [LCS](/mobilnisite/slovnik/lcs/)) a přidružených bezpečnostních protokolů. Tím byl vytvořen business-to-business ([B2B](/mobilnisite/slovnik/b2b/)) model pro služby, který motivoval vznik živého ekosystému služeb založených na poloze, multimediálních zpráv a později širších IoT a [API](/mobilnisite/slovnik/api/) služeb. Byl to základní krok ve vývoji od uzavřených telekomunikačních sítí k otevřeným platformám.

## Klíčové vlastnosti

- Definován jako externí aplikační poskytovatel v servisních architekturách 3GPP
- Přistupuje k síťovým schopnostem prostřednictvím standardizovaných otevřených rozhraní (např. Le, Mm1)
- Hostuje aplikační logiku a platformy pro poskytování služeb
- Podléhá bezpečnostním a ochranným politikám definovaným ve specifikacích 3GPP
- Klíčový aktér v ekosystémech Location Services (LCS) a MMS
- Umožňuje inovace služeb třetích stran využívající síťové enablery

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [WSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/wsp/)
