---
slug: "gsf"
url: "/mobilnisite/slovnik/gsf/"
type: "slovnik"
title: "GSF – Generic Security Functionality"
date: 2025-01-01
abbr: "GSF"
fullName: "Generic Security Functionality"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/gsf/"
summary: "Generic Security Functionality (GSF) je bezpečnostní rámec 3GPP, který poskytuje standardizovanou, modulární sadu kryptografických funkcí a bezpečnostních protokolů pro ochranu dat v uživatelské rovin"
---

GSF je bezpečnostní rámec 3GPP, který poskytuje standardizovanou, modulární sadu kryptografických funkcí a bezpečnostních protokolů pro ochranu dat v uživatelské rovině, umožňující algoritmicky agilní šifrování a ochranu integrity.

## Popis

Generic Security Functionality (GSF) je bezpečnostní architektura definovaná v 3GPP, primárně v bezpečnostní specifikaci TS 33.805 a souvisejících dokumentech. Je navržena tak, aby poskytovala obecnou, znovupoužitelnou sadu bezpečnostních funkcí pro ochranu důvěrnosti a integrity datových toků v uživatelské rovině. Na rozdíl od bezpečnostních protokolů vázaných na konkrétní rádiové přístupové technologie (jako je zabezpečení [NAS](/mobilnisite/slovnik/nas/) nebo [RRC](/mobilnisite/slovnik/rrc/) v řídicí rovině) je GSF agnostická vůči aplikaci i transportu. Funguje jako bezpečnostní vrstva, kterou lze aplikovat na různé datové toky, jako jsou mediální streamy v IMS nebo data zachycená pro účely zákonného odposlechu.

Architektonicky je GSF postavena na modulárním konceptu kryptografických transformací a rámci správy klíčů. Základní komponenty zahrnují GSF entitu, která implementuje kryptografické funkce, a entitu správy klíčů (KME) zodpovědnou za bezpečnou derivaci a distribuci klíčů. GSF entita používá kryptografické algoritmy (např. [AES](/mobilnisite/slovnik/aes/) v režimu [CTR](/mobilnisite/slovnik/ctr/) pro šifrování, HMAC-SHA-256 pro integritu) ke zpracování dat. Funguje tak, že vezme otevřená uživatelská data a sadu bezpečnostních klíčů (např. [CK](/mobilnisite/slovnik/ck/), [IK](/mobilnisite/slovnik/ik/) odvozené z [AKA](/mobilnisite/slovnik/aka/) nebo speciálně zřízené klíče) a aplikuje nakonfigurovanou kryptografickou transformaci pro vygenerování chráněného datového paketu, který může obsahovat značky integrity. Příjemající GSF entita provede zpětnou operaci pomocí stejných klíčů.

Jak to funguje, zahrnuje několik vrstev. Nejprve dojde k navázání klíče, často s využitím existujících bezpečnostních kontextů 3GPP (z AKA) nebo prostřednictvím samostatného protokolu pro dohodu klíče. Jakmile jsou klíče navázány, je zpracován datový tok. Pro každý datový paket (např. IP paket nebo mediální rámec) GSF aplikuje šifrovací a/nebo integritní algoritmus podle definovaného formátu paketu, který zahrnuje potřebné hlavičky, jako jsou sekvenční čísla pro prevenci replay útoků. Specifikace definuje formáty paketů (jako GSF-PDU) pro přenos tohoto zabezpečeného payloadu. Tento proces je nezávislý na tom, zda jsou data transportována přes UDP, TCP nebo jiné prostředky.

Její role v síti je zvláště významná ve dvou oblastech: zákonný odposlech ([LI](/mobilnisite/slovnik/li/)) a zabezpečené doručování médií. V LI (specifikováno v TS 33.805) se GSF používá k šifrování zachyceného obsahu mezi mediační funkcí sítě a monitorovacím zařízením orgánů činných v trestním řízení, což zajišťuje důvěrnost zachycených dat během přenosu. Pro služby jako Multimedia Broadcast/Multicast Service (MBMS) nebo média IMS může GSF poskytnout dodatečnou vrstvu end-to-end zabezpečení nad rámec ochrany přístupové sítě. Poskytuje standardizovaný způsob, jak dosáhnout algoritmické agilnosti, což umožňuje sítím aktualizovat kryptografické algoritmy bez změny základní logiky služby.

## K čemu slouží

Generic Security Functionality (GSF) byla vytvořena k řešení potřeby flexibilního, standardizovaného bezpečnostního mechanismu pro data v uživatelské rovině, který není inherentně vázán na specifické zabezpečení rádiového přístupového beareru. Před GSF vyžadovalo zabezpečení aplikačních dat často proprietární nebo služebně specifická řešení, což vedlo k fragmentaci, zvýšené složitosti a potenciálním zranitelnostem. Existovala jasná mezera pro obecnou, znovupoužitelnou bezpečnostní vrstvu, kterou by bylo možné aplikovat napříč různými službami 3GPP a síťovými rozhraními.

Hlavním hybatelem byly vyvíjející se požadavky na zákonný odposlech (LI). Regulátoři požadovali zabezpečené doručování zachycené komunikace ze sítě operátora k orgánům činným v trestním řízení. Tento přenos vyžadoval silné, standardizované šifrování pro ochranu samotných citlivých zachycených dat. GSF poskytla standardizované řešení 3GPP pro tento spoj, zajišťující interoperabilitu mezi odposlechovými systémy různých dodavatelů a splňující regulatorní bezpečnostní záruky. Vyřešila problém, jak bezpečně transportovat zachycený obsah přes potenciálně nedůvěryhodné sítě mezi operátorem a orgány.

Kromě toho vzestup IP-based multimediálních služeb (IMS) a vysílacích služeb (MBMS) vytvořil potřebu konzistentní ochrany obsahu. Zatímco přístupové zabezpečení (např. AS a NAS zabezpečení v LTE) chrání spojení k UE, neposkytuje end-to-end zabezpečení pro samotný mediální tok. GSF nabídla modulární rámec pro aplikaci důvěrnosti a integrity na tyto toky, nezávisle na podkladovém transportním protokolu (RTP, UDP atd.). Její vytvoření bylo motivováno snahou o algoritmickou agilitu – umožnění aktualizace kryptografických algoritmů s vývojem hrozeb bez přepracování celé servisní architektury – a o čisté oddělení mezi bezpečnostními funkcemi a aplikační logikou, což podporuje bezpečnější a udržovatelnější návrh systémů.

## Klíčové vlastnosti

- Poskytuje obecné, na transportu nezávislé šifrování a ochranu integrity pro data v uživatelské rovině
- Modulární architektura podporující více kryptografických algoritmů (např. AES, SNOW 3G)
- Definuje standardizované formáty paketů (GSF-PDU) pro přenos zabezpečených payloadů
- Integruje se se správou klíčů 3GPP, využívá klíče z AKA nebo dedikované derivace klíčů
- Kritická enabling technologie pro zabezpečená rozhraní doručování zákonného odposlechu (LI)
- Podporuje algoritmickou agilitu, umožňující kryptografické aktualizace bez narušení služby

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [GSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/gsf/)
