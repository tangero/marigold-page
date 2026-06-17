---
slug: "e2ee"
url: "/mobilnisite/slovnik/e2ee/"
type: "slovnik"
title: "E2EE – End-to-End Encryption"
date: 2026-01-01
abbr: "E2EE"
fullName: "End-to-End Encryption"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/e2ee/"
summary: "E2EE je bezpečnostní metoda, při níž jsou data zašifrována na zařízení odesílatele a dešifrována pouze na zařízení příjemce, což zabraňuje přístupu zprostředkovatelů, jako jsou síťoví operátoři nebo p"
---

E2EE je bezpečnostní metoda pro uživatelské komunikační služby, jako je zasílání zpráv a volání, při níž jsou data zašifrována na zařízení odesílatele a dešifrována pouze na zařízení příjemce, což zajišťuje soukromí vůči zprostředkovatelům a poskytovatelům infrastruktury.

## Popis

End-to-End Encryption (E2EE) ve standardech 3GPP je bezpečnostní paradigma uplatňované primárně u komunikačních služeb, kde je kryptografická ochrana aplikována na výchozím uživatelském zařízení (UE) a je odstraněna až na cílovém UE nebo zamýšlené aplikaci. Šifrovací a dešifrovací klíče jsou výhradně pod kontrolou komunikujících koncových bodů; nejsou přístupné síťovým uzlům, včetně prvků rádiové přístupové sítě (RAN), funkcí jádra sítě nebo aplikačních serverů provozovaných poskytovatelem služby. Tím je zajištěno, že obsah komunikace (např. text, hlas, video, soubory) zůstane důvěrný pro všechny strany kromě zamýšleného odesílatele a příjemce, což poskytuje silnou garanci soukromí.

Z architektonického hlediska je E2EE dle 3GPP implementována na aplikační vrstvě, odděleně od základní přístupové bezpečnosti poskytované sítí (jako je bezpečnost [NAS](/mobilnisite/slovnik/nas/) a [AS](/mobilnisite/slovnik/as/) v 5G). Standardy, například pro IP Multimedia Subsystem (IMS) a konverzační služby, definují protokoly a postupy pro správu klíčů a zabezpečenou výměnu médií. Typický systém E2EE zahrnuje několik klíčových komponent: systém správy identit a klíčů (často založený na infrastruktuře veřejného klíče), protokol pro dohodu klíče (jako Diffie-Hellman nebo jeho varianty na eliptických křivkách) a protokol pro šifrování médií (například [SRTP](/mobilnisite/slovnik/srtp/) pro hlas/video). Specifikace 3GPP definují, jak se tyto komponenty integrují s existujícími postupy IMS pro registraci, zahájení relace (prostřednictvím SIP) a vyjednávání médií.

Proces funguje následovně: Nejprve se uživatelé musí ověřit u služby a případně si vyměnit dlouhodobé veřejné klíče nebo identifikační klíče. Při zahájení zabezpečené relace (např. volání nebo chatu) se koncové body zapojí do protokolu pro dohodu klíče, který je často integrován do signalizace relace (např. v rámci zpráv SIP/SDP). Výsledkem je sdílený tajný relací klíč známý pouze oběma UE. Všechny pakety médií jsou poté před odesláním přes síť zašifrovány tímto klíčem pomocí symetrické šifry (jako [AES](/mobilnisite/slovnik/aes/)). Jádro IMS ([CSCF](/mobilnisite/slovnik/cscf/) atd.) a mediální brány přeposílají zašifrované signalizační a mediální pakety, ale nemohou je dešifrovat. Některé systémy také poskytují dopřednou utajenost tím, že pravidelně generují nové relací klíče.

Úlohou E2EE v síti je poskytnout doplňkovou, uživatelsky orientovanou vrstvu zabezpečení nad rámec bezpečnosti poskytované sítí. Zatímco přístupová bezpečnost sítě chrání rádiový spoj a signalizaci v jádru sítě před odposlechem, E2EE chrání obsah před samotným poskytovatelem služby a případně kompromitovanými síťovými prvky. To je zásadní pro budování důvěry uživatelů, zejména u citlivých komunikací. Umožňuje také splnění přísných předpisů na ochranu dat. Správa E2EE, včetně distribuce a ověřování klíčů (např. porovnáním otisků klíčů), je navržena tak, aby byla uživatelsky přívětivá, často integrovaná do klientské aplikace služby.

## K čemu slouží

End-to-End Encryption (E2EE) byla do standardů 3GPP zavedena počínaje Release 14 primárně proto, aby reagovala na rostoucí požadavky na soukromí uživatelů a poskytla robustnější bezpečnostní model pro konverzační služby. Tradiční zabezpečení mobilních sítí, ačkoli je robustní pro přístup a signalizaci, končí na okraji sítě – data jsou v jádru sítě operátora dešifrována za účelem zpracování, směrování nebo zákonného odposlechu. Tento model inherentně důvěřuje síťovému operátorovi a poskytovateli služby s otevřeným textem obsahu, což se stalo problémem s nástupem všudypřítomné digitální komunikace a veřejně známých narušení dat.

Motivace pro standardizaci E2EE byla mnohostranná. Za prvé, uživatelské aplikace pro zasílání zpráv, jako WhatsApp a Signal, popularizovaly E2EE a zvýšily tak uživatelská očekávání ohledně soukromí ve všech komunikačních službách, včetně těch poskytovaných telekomunikačními operátory. Za druhé, regulační prostředí, jako je GDPR v Evropě, zdůraznilo minimalizaci dat a ochranu soukromí již při návrhu, což tlačilo na technická opatření omezující přístup poskytovatelů služeb k osobním údajům. E2EE to řeší přímo tím, že činí obsah pro poskytovatele nepřístupným. Za třetí, zmírňuje rizika spojená s centralizovaným ukládáním dat; narušení serverů operátora by neohrozilo obsah komunikací chráněných E2EE.

Před standardizovanou E2EE postrádaly služby obohacené komunikace (RCS) a služby založené na IMS poskytované operátory tuto úroveň ochrany soukromí obsahu. Omezení spočívalo v tom, že zabezpečení končilo na síťové bráně. Cílem standardizace bylo poskytnout interoperabilní řešení E2EE na úrovni operátora, které by mohlo být integrováno do IMS a dalších servisních rámců 3GPP, což by operátorům umožnilo nabízet konkurenceschopné a bezpečné služby. Řešila tak problém udržení důvěry uživatelů v éře, kdy síťový operátor již není jedinou – nebo nejdůvěryhodnější – stranou v komunikačním řetězci.

## Klíčové vlastnosti

- Šifrování a dešifrování probíhá výhradně na koncových uživatelských zařízeních, nikoli na síťových uzlech
- Používá asymetrickou kryptografii pro dohodu klíče (např. Elliptic Curve Diffie-Hellman)
- Poskytuje dopřednou utajenost, kdy kompromitace dlouhodobých klíčů neodhalí předchozí relace
- Integruje se se signalizací IMS (SIP/SDP) pro vyjednání klíče v rámci pásma
- Podporuje šifrování médií pro hlasový, video a textový obsah
- Obsahuje mechanismy pro ověření klíče (např. porovnání otisku) k prevenci útoků typu man-in-the-middle

## Definující specifikace

- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TS 24.883** (Rel-16) — MCPTT Interworking with LMR Systems

---

📖 **Anglický originál a plná specifikace:** [E2EE na 3GPP Explorer](https://3gpp-explorer.com/glossary/e2ee/)
