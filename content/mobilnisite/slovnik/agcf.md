---
slug: "agcf"
url: "/mobilnisite/slovnik/agcf/"
type: "slovnik"
title: "AGCF – Access Gateway Control Function"
date: 2025-01-01
abbr: "AGCF"
fullName: "Access Gateway Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/agcf/"
summary: "Access Gateway Control Function (AGCF) je prvek jádra sítě v IP Multimedia Subsystem (IMS), který poskytuje řídicí a interworking funkce pro legacy přístupové sítě nepodporující IMS, jako jsou PSTN/IS"
---

AGCF je prvek jádra sítě IMS, který řídí a zprostředkovává spolupráci s legacy přístupovými sítěmi nepodporujícími IMS, překládá jejich signalizační protokoly na SIP protokol IMS, aby umožnil migraci na plně IP architekturu.

## Popis

Access Gateway Control Function (AGCF) je klíčová komponenta v architektuře IP Multimedia Subsystem (IMS) podle 3GPP, speciálně navržená k propojení legacy okruhově přepínaných a analogových přístupových sítí s moderním paketově přepínaným jádrem IMS. Funguje jako specializovaný Session Initiation Protocol (SIP) User Agent a řídicí prvek mediální brány. Architektonicky se AGCF nachází v řídicí rovině IMS a na straně uživatele komunikuje s Media Gateways (MGWs) nebo Residential Gateways (RGs) pomocí protokolu H.248 (Megaco) pro řízení médií. Na straně sítě komunikuje s dalšími prvky jádra IMS, jako je Serving-Call Session Control Function (S-CSCF) a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), pomocí standardizovaných rozhraní IMS založených na SIP (např. Gm, Mw). Její primární role spočívá v emulaci terminálu IMS pro skupinu účastníků nepodporujících IMS, což jim umožňuje se vůči jádru sítě jevit jako nativní uživatelé IMS.

Operačně AGCF provádí překlad protokolů a zprostředkování spolupráce. Když legacy terminál zahájí hovor, přidružená Media Gateway odešle přes H.248 řídicí zprávy do AGCF. AGCF tyto zprávy přeloží na příslušné metody SIP (např. INVITE, REGISTER) a přepošle je do jádra IMS. Opačně je signalizace SIP z IMS určená pro legacy uživatele přeložena AGCF zpět na příkazy H.248, aby nařídila Media Gateway vytvořit příslušnou přenosovou cestu. AGCF spravuje registrační stav připojených legacy linek, zpracovává předplatitelská data a implementuje potřebné procedury IMS, jako je autentizace a spouštění služeb, jménem těchto uživatelů.

Klíčové vnitřní komponenty AGCF zahrnují H.248 Control Function pro správu mediálních bran, SIP User Agent pro komunikaci s IMS a interworking logiku pro mapování mezi oběma doménami. Je zodpovědná za celý životní cyklus relace, včetně zahájení, ukončení a funkcí během hovoru pro legacy uživatele. Tím, že abstrahuje komplexitu legacy přístupu, umožňuje AGCF síťovým operátorům zavádět služby založené na IMS – jako je VoLTE, videohovory a rich communication services (RCS) – pro širokou zákaznickou základnu bez nutnosti okamžité modernizace veškerého koncového zařízení na straně zákazníka, což umožňuje nákladově efektivní a postupný přechod sítě.

## K čemu slouží

AGCF byla vytvořena, aby řešila zásadní výzvu při migraci telekomunikačního průmyslu od tradiční okruhově přepínané telefonie (PSTN/[ISDN](/mobilnisite/slovnik/isdn/)) k plně IP architektuře IMS. Před IMS byly hlasové služby poskytovány přes vyhrazené, izolované sítě používající protokoly jako ISDN User Part ([ISUP](/mobilnisite/slovnik/isup/)) a Q.931. Zavedení IMS slibovalo sjednocené, službami bohaté jádro založené na IP, ale vytvořilo mezeru v interoperabilitě pro obrovskou instalovanou základnu legacy analogových a digitálních terminálů, PBX systémů a přístupových sítí. Nasazení IMS bez migrační cesty by tyto prostředky izolovalo a narušilo služby pro miliony uživatelů.

Primární problém, který AGCF řeší, je umožnění připojení těchto legacy přístupových sítí a koncových bodů k IMS službám a jejich využívání. Poskytuje nezbytné řízení a signalizační zprostředkování spolupráce, což síťovým operátorům umožňuje modernizovat svá jádra sítí na IMS při zachování investic do stávající přístupové infrastruktury a koncového zařízení zákazníků. To usnadnilo postupnou, ekonomicky životaschopnou evoluci sítě. Motivací byla potřeba kontinuity služeb, snížení kapitálových výdajů během přechodu a schopnost zavádět nové služby založené na IP pro všechny účastníky, nejen pro ty s nativními zařízeními IMS. Historicky podobné funkce brány existovaly v sítích před IMS, ale AGCF tuto funkci standardizovala v rámci frameworku IMS 3GPP počínaje Release 10, čímž poskytla jasnou architektonickou definici a rozhraní pro škálovatelné, provozně robustní zprostředkování spolupráce.

## Klíčové vlastnosti

- Zprostředkování spolupráce protokolů mezi H.248 (Megaco) a IMS SIP
- Vystupuje jako SIP User Agent jménem účastníků nepodporujících IMS
- Řízení Media Gateway (MGWs) a Residential Gateway (RGs) pro vytváření přenosových cest
- Registrace, autentizace a správa relací pro legacy přístupové linky
- Umožňuje poskytování služeb IMS (např. hlas, video) účastníkům PSTN/ISDN a analogovým účastníkům
- Podporuje postupnou migraci sítě z okruhově přepínaného na plně IP jádro IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework

---

📖 **Anglický originál a plná specifikace:** [AGCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/agcf/)
