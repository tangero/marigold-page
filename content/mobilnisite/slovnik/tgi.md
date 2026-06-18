---
slug: "tgi"
url: "/mobilnisite/slovnik/tgi/"
type: "slovnik"
title: "TGI – Temporary MCVideo Group Identity"
date: 2025-01-01
abbr: "TGI"
fullName: "Temporary MCVideo Group Identity"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tgi/"
summary: "Dočasný identifikátor přidělený konkrétní skupinové relaci v rámci služby Mission Critical Video (MCVideo). Jednoznačně identifikuje skupinové volání pro videokomunikaci mezi uživateli z oblasti veřej"
---

TGI (Temporary MCVideo Group Identity) je dočasný identifikátor, který jednoznačně identifikuje konkrétní skupinovou relaci pro videokomunikaci v rámci služby Mission Critical Video (MCVideo).

## Popis

Temporary [MCVideo](/mobilnisite/slovnik/mcvideo/) Group Identity (TGI) je klíčový identifikátor v rámci architektury služeb Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)) podle 3GPP, konkrétně pro službu MCVideo. MCVideo poskytuje skupinovou videokomunikaci v reálném čase pro složky veřejné bezpečnosti, záchranné služby a další uživatele s kritickým nasazením. TGI je dočasný, na relaci specifický identifikátor přidělený systémem MCVideo konkrétnímu skupinovému hovoru nebo videoschůzce. Používá se k jednoznačnému odlišení této relace od všech ostatních probíhajících relací v síti po dobu její aktivity. Na rozdíl od trvalého skupinového ID (které identifikuje předdefinovanou skupinu uživatelů) identifikuje TGI samotnou aktivní komunikační instanci.

Z architektonického hlediska je TGI generován a spravován hlavními komponentami služby MCVideo, především MCVideo Application Server. Když autorizovaný uživatel (např. dispečer nebo velitel týmu) zahájí skupinové videovolání, server pro tuto relaci přidělí TGI. Tento TGI je poté rozeslán do User Equipment (UE) všech účastníků a příslušných síťových funkcí. Používá se v signalizační rovině pro směrování zpráv řízení relace (např. pomocí protokolů [SIP](/mobilnisite/slovnik/sip/)) a v mediální rovině pro identifikaci mediálních proudů spojených s hovorem. TGI je zahrnut v protokolových zprávách pro zřizování, modifikaci a ukončení relace, čímž zajišťuje, že všechny akce se vztahují ke správné relaci.

Jak to funguje, zahrnuje několik vrstev. Na servisní vrstvě klient MCVideo na UE přijme TGI během signalizace zahájení relace. UE používá toto TGI ve veškeré následné komunikaci se serverem MCVideo. V podkladovém systému 3GPP může být TGI mapován nebo asociován se specifickými přenosovými kanály nebo QoS toky, aby bylo zajištěno, že videoprovoz obdrží odpovídající prioritu a prostředky dle požadavků QoS pro kritické nasazení. Z bezpečnostního hlediska je TGI součástí bezpečnostního kontextu; může být použit při odvozování klíčů pro šifrování videomedií, čímž zajišťuje důvěrnost v rámci této konkrétní skupinové relace. Jeho dočasná povaha je klíčová – je platný pouze po dobu životnosti hovoru. Jakmile relace skončí, TGI může být uvolněno a potenciálně znovu použito později pro jinou relaci, což napomáhá správě prostředků a zabraňuje vyčerpání identifikátorů.

## K čemu slouží

TGI bylo vytvořeno, aby řešilo specifické potřeby dynamické, zabezpečené a spravovatelné skupinové komunikace v prostředích s kritickým nasazením. Tradiční skupinové hovory v buňkových sítích nebo konferenční systémy často postrádaly standardizovaný, zabezpečený a dočasný identifikátor vyhrazený pro jednu instanci relace. Operace s kritickým nasazením vyžadují schopnost rychle vytvářet ad-hoc videoskupiny, zajistit, aby komunikace byla izolovaná a zabezpečená pro danou skupinu, a efektivně spravovat více současně probíhajících incidentů nebo operací. Samotné trvalé skupinové identity nestačí, protože stejná skupina uživatelů může být současně zapojena do více různých videoschůzek (např. různých taktických operací).

Účelem TGI je poskytnout systému prostředek pro jedinečnou správu každé aktivní relace. Řeší problémy rozlišení relací, zabezpečeného propojení médií a efektivního směrování. Historicky proprietární systémy nebo rané služby skupinové komunikace mohly používat méně robustní metody, což vedlo k potenciálním zmatkům nebo bezpečnostním záměnám. TGI, zavedené jako součást standardizované služby 3GPP [MCVideo](/mobilnisite/slovnik/mcvideo/) od Release 13 výše, poskytuje čistý, škálovatelný mechanismus. Motivací byly požadavky komunity veřejné bezpečnosti (vedené organizacemi jako [TCCA](/mobilnisite/slovnik/tcca/) a 3GPP SA6) na interoperabilní, spolehlivou a bezpečnou komunikaci s kritickým nasazením založenou na LTE. TGI umožňuje funkce jako dynamické vytváření skupin, striktní řízení přístupu ke konkrétní relaci a koncově šifrovaná média pro tuto relaci, které jsou klíčové pro práci policie, hasičů a záchranné zdravotní služby.

## Klíčové vlastnosti

- Jednoznačně identifikuje aktivní instanci skupinové relace MCVideo
- Dočasná platnost omezená na dobu trvání relace
- Přiděluje a spravuje ho MCVideo Application Server
- Používá se pro směrování signalizace relace a identifikaci mediálních proudů
- Integrální součást bezpečnostního kontextu relace pro odvozování klíčů
- Umožňuje správu více souběžných relací pro stejnou skupinu uživatelů

## Související pojmy

- [MCVideo – Mission Critical Video](/mobilnisite/slovnik/mcvideo/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [TGI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tgi/)
