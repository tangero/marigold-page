---
slug: "mpc"
url: "/mobilnisite/slovnik/mpc/"
type: "slovnik"
title: "MPC – Media Preconfigured Channel"
date: 2025-01-01
abbr: "MPC"
fullName: "Media Preconfigured Channel"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mpc/"
summary: "MPC je síťová schopnost, která předem zřizuje přenosové prostředky (bearer) pro mediální tok před žádostí uživatele o službu, čímž umožňuje ultranízkou latenci pro kritické komunikace. Je klíčovým prv"
---

MPC je síťová schopnost, která předem zřizuje přenosové prostředky (bearer) pro mediální tok před žádostí uživatele o službu, aby umožnila ultranízkou latenci pro kritické komunikace, jako je Mission Critical Push-To-Talk.

## Popis

Media Preconfigured Channel (MPC) je architektonická funkce sítě navržená pro podporu ultranízké latence a okamžitého zřízení média pro služby kritické komunikace, zejména Mission Critical Push-To-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) definovaný 3GPP. Funguje na principu předběžného zřízení potřebných přenosových prostředků (bearer) – logické komunikační cesty s definovanou kvalitou služeb (QoS) – mezi síťovými entitami *předtím*, než je potřeba přenášet skutečné médium (hlas, video, data). Tato předkonfigurace eliminuje signalizační zpoždění typicky spojené se zřizováním beareru při zahájení hovoru, které může činit stovky milisekund, a tím dosahuje téměř okamžitého přenosu média.

Architektonicky MPC zahrnuje koordinaci mezi jádrem sítě a rádiovou přístupovou sítí (RAN). Pro skupinu uživatelů předplacených na službu kritické komunikace síť proaktivně vytvoří předkonfigurovaný kontext beareru. Tento kontext zahrnuje všechny potřebné parametry QoS (jako QoS Class Identifier, Guaranteed Bit Rate), identifikátory koncových bodů tunelů (pro [GTP](/mobilnisite/slovnik/gtp/) tunely v jádru) a rádiové prostředky. Kontext je uložen v příslušných síťových funkcích: User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v 5G Core, nebo [PGW](/mobilnisite/slovnik/pgw/) a [SGW](/mobilnisite/slovnik/sgw/) v EPC, stejně jako v základnové stanici (gNB nebo [eNB](/mobilnisite/slovnik/enb/)). Bearer zůstává v 'nečinném' nebo 'spícím' stavu, spotřebovávaje minimální prostředky, dokud není aktivován.

Mechanismus funguje ve spolupráci se signalizací na aplikační vrstvě. Když uživatel MCPTT stiskne tlačítko pro vysílání (push-to-talk), aplikační vrstva (MCPTT aplikační server) odešle žádost o aktivaci. Protože je bearer již předkonfigurován, síť může okamžitě namapovat mediální tok na existující přenosové prostředky. RAN může rychle převést rádiové spojení uživatele z nečinného stavu do aktivního, nebo přidělit předem rezervované rádiové prostředky, a UPF může začít přeposílat pakety přes předem zřízené GTP tunely. To vede k extrémně nízké koncové latenci ([E2E](/mobilnisite/slovnik/e2e/)) pro první mediální paket. MPC je řízen prostřednictvím procedur definovaných 3GPP zahrnujících Policy Control Function (PCF) pro autorizaci předkonfigurace a Unified Data Management (UDM) pro data účastníka. Specifikace jako TS 23.167 a TS 29.163 detailně popisují signalizační toky a interakce mezi aplikační vrstvou, jádrem sítě a RAN pro vytváření, správu a aktivaci těchto předkonfigurovaných kanálů.

## K čemu slouží

MPC bylo vytvořeno k řešení základního problému latence v tradičních mobilních sítích pro služby kritické komunikace a interaktivní služby v reálném čase. Standardní hlasové a datové relace v mobilních sítích zřizují přenosové cesty (bearer) na vyžádání, když uživatel zahájí hovor nebo datovou relaci. Toto zřizování zahrnuje několik signalizačních kroků mezi zařízením, RAN a jádrem sítě, což zavádí zpoždění, které je často nepřijatelné pro kritické scénáře, jako je veřejná bezpečnost, kde může být půlvteřinové zpoždění v konverzaci push-to-talk nebezpečné. Existující architektura LTE/EPC byla optimalizována pro efektivitu, nikoli pro okamžitost vyžadovanou záchrannými složkami.

Hlavním hybatelem byla standardizace Mission Critical Services (MCS) přes LTE, počínaje 3GPP Release 13. MCPTT, jako vlajková služba, vyžadoval dobu zřízení hovoru včetně vytvoření mediální cesty pod 300 ms. Tradiční procedura zřizování beareru nemohla tohoto cíle dosáhnout. MPC to řeší přesunutím práce na vytvoření cesty kritické z hlediska latence do doby, kdy latence není kritická – například když se uživatel zaregistruje ke službě nebo připojí do mluvčí skupiny – takže když nastane naléhavý okamžik, je cesta připravena k použití. V podstatě vyměňuje malé množství trvalé rezervace prostředků za masivní snížení reakční doby.

MPC navíc umožňuje efektivní skupinovou komunikaci. Pro velkou mluvčí skupinu umožňuje předkonfigurace sdíleného multicast/broadcast beareru (jako evolved Multimedia Broadcast Multicast Service - eMBMS) jako MPC všem členům skupiny přijímat médium okamžitě při jeho vysílání, bez zpoždění individuálního zřizování unicastu. Tento vývoj představuje významný posun v síťové filozofii návrhu, od čistě alokace prostředků na vyžádání k prediktivnímu a preventivnímu řízení prostředků pro podporu aplikací citlivých na latenci a životně důležitých aplikací přes komerční mobilní infrastrukturu.

## Klíčové vlastnosti

- Předem zřizuje přenosové prostředky (bearer) (QoS, tunely, rádiový kontext) před skutečným přenosem média, aby eliminovala zpoždění při zřizování
- Umožňuje ultranízkou latenci při zřizování média pro Mission Critical Push-To-Talk (MCPTT) a další kritické služby
- Zahrnuje koordinaci mezi aplikační vrstvou, jádrem sítě 5GC/EPC a RAN pro koncovou předkonfiguraci
- Podporuje jak unicastové, tak multicast/broadcastové (eMBMS) předkonfigurované kanály pro skupinovou komunikaci
- Bearer zůstává v nečinném (spícím) stavu, dokud není aktivován spouštěčem z aplikační vrstvy, čímž šetří prostředky, když je nečinný
- Standardizováno v 3GPP pro integraci s funkcemi řízení politik (PCF) a správy relací (SMF)

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 29.863** (Rel-8) — IMS-CS Multimedia Interworking Feasibility Study
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [MPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpc/)
